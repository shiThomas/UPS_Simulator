import socket
import select
import sys
import time
import psycopg2
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint, _VarintBytes
from proto import world_ups_pb2
from proto import ups_amazon_pb2
import build_commands
import build_ups_amazon_commands
import threading
from handle_request import *

# UPS_HOST = socket.gethostname()
# UPS_PORT = 54321
# WORLD_HOST = 'vcm-9320.vm.duke.edu'
# WORLD_PORT = 12345

WORLD_HOST = 'vcm-9229.vm.duke.edu'
WORLD_PORT = 12345

# AMAZON_HOST = '10.197.193.1'
# AMAZON_PORT = 44555

AMAZON_HOST = '10.197.40.0'
AMAZON_PORT = 7893

# AMAZON_HOST = 'vcm-9448.vm.duke.edu'
# AMAZON_PORT = 12345

idle = 1
traveling = 2
arrive_warehouse = 3
loading = 4
loaded = 5
delivering = 6

prepare_for_delivery = 0
in_transit = 1
package_delivered = 2

ack_set = set()
# ack_set.add(x)
# ack_set.remove(x)

sleep_time = 5

dbcursor = 0

world_socket = None
amazon_socket = None

world_seqnum = 0
amazon_seqnum = 0
NUM_TRUCK_INIT = 1000

# To do list:
# 0. connect to Database.
# 1. connect to world.
# 2. initialize trucks
# 3. receive warehouse ID
# 4. Send go pick up signal to trucks
# 5. Receive Truck ID, WareHouse ID, Status from trucks
# 6. Send Truck ID to Amazon
# 7. Receive Destination ID and shipping location
# 8. Generate Package ID
# 9. Send go Deliver to trucks.

# Connect to Database.
def connect_db():
    while True:
        try:
            dbconn = psycopg2.connect(
                database = 'xwqawgaa',
                user = 'xwqawgaa',
                password = 'nmErOf1YehpHpldPYghZpaNTdu_RIxUJ',
                host = 'isilo.db.elephantsql.com',
                port = '5432')
            # cur = dbconn.cursor()
            # print('Successfully connected to the database')
            return dbconn
        except:
            # print('Unable to connect to the database')
            continue
        
# Connect World
def connect_world_server():
    world_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    world_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:
        try:
            world_socket.connect((WORLD_HOST, WORLD_PORT))
            print('Successfully connected to World Server')
            return world_socket
        except:
            print('Unable to connect to World Server')
            continue

# Connect to World or create a new World
def connect_world(world_socket, worldid, num_truck_init):
    # Connect to database
    dbconn = connect_db()
    dbcursor = dbconn.cursor()
    
    u_connect = world_ups_pb2.UConnect()
    u_connect.isAmazon = False
    if worldid:
        u_connect.worldid = int(worldid)
        send_msg(world_socket, u_connect)
    else:
        dbcursor.execute("delete from myapp_truck")
        dbcursor.execute("delete from myapp_package")
        
        for i in range(0, num_truck_init):
            trucks = u_connect.trucks.add()
            trucks.id = i
            trucks.x = 0
            trucks.y = 0

            dbcursor.execute(
                "insert into myapp_truck" +
                "(truck_id, truck_status) " +
                "values ('" +
                str(i) + "', '" +
                str(idle) + "')")

        dbconn.commit()
        send_msg(world_socket, u_connect)
        
    # response = recv_msg(world_socket)
    u_connected = world_ups_pb2.UConnected()
    u_connected = recv_msg(world_socket, u_connected)
    # u_connected.ParseFromString(response)

    dbcursor.close()
    dbconn.close()
    return u_connected.worldid, u_connected.result

# Receive UResponses from world
def recv_world(world_socket):
    response = recv_msg(world_socket)
    u_responses = world_ups_pb2.UResponses()
    u_responses.ParseFromString(response)
    return u_responses

# Receive AUCommands from Amazon
def recv_amazon(amazon_socket):
    response = recv_msg(amazon_socket)
    au_commands = ups_amazon_pb2.AUCommands()
    au_commands.ParseFromString(response)
    print('The response from Amazon-----------')
    print(au_commands)
    print('-----------------------------------')
    return au_commands

# Connect Amazon
def connect_amazon():
    amazon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    amazon_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:
        try:
            amazon_socket.connect((AMAZON_HOST, AMAZON_PORT))
            print('Successfully connected to Amazon')
            return amazon_socket
        except:
            print('Unable to connect to Amazon')
            continue

# Send with encoded length info
def send_msg(s, msg):
    hdr = []
    _EncodeVarint(hdr.append, len(msg.SerializeToString()), None)
    s.send(b"".join(hdr))
    s.send(msg.SerializeToString())

"""
def send_msg(skt, obj):
    size = obj.ByteSize()
    skt.send(_VarintBytes(size))
    temp = obj.SerializeToString()
    skt.send(temp)
"""

# Recv with encoded length info
def recv_msg(s, msg):
    var_int_buff = []
    while True:
        try:
            buf = s.recv(1)
            var_int_buff += buf
            msg_len, new_pos = _DecodeVarint32(var_int_buff, 0)
            if new_pos != 0:
                break
        except IndexError:
            pass
        except socket.error:
            pass
    whole_message = []

    print('msg_len is:', msg_len)
    while True:
        data = s.recv(msg_len)
        whole_message.append(data)
        msg_len -= len(data)
        if msg_len is 0 :
            break

    msg.ParseFromString(b"".join(whole_message))
    return msg

# Reply ack to Amazon
def return_ack_to_amazon(amazon_socket, seqnum):
    ua_commands = ups_amazon_pb2.UACommands()
    ua_commands.ack[:] = [seqnum]
    send_msg(amazon_socket, ua_commands)

# Reply ack to world(seqnum):
def return_ack_to_world(world_socket, seqnum):
    u_commands = world_ups_pb2.UCommands()
    u_commands.acks[:] = [seqnum]
    send_msg(world_socket, u_commands)
    
# Handle messages from world
def handle_world(amazon_socket, world_socket):
    global ack_set
    global amazon_seqnum
    global world_seqnum
    
    # Read from world_socket
    u_responses = world_ups_pb2.UResponses()
    u_responses = recv_msg(world_socket, u_responses)
    # u_responses = recv_world(world_socket)
    print(u_responses)
    completion_size = len(u_responses.completions)
    for completion in u_responses.completions:
        t = threading.Thread(
            target = handle_completion,
            args = (amazon_socket, world_socket, completion, amazon_seqnum))
        amazon_seqnum += completion_size
        t.start()
    for delivered in u_responses.delivered:
        t = threading.Thread(
            target = handle_delivered,
            args = (amazon_socket, world_socket, delivered, amazon_seqnum))
        amazon_seqnum += 1
        t.start()
    for ack in u_responses.acks:
        print('Received ack from world:', ack)
        ack_set.add(ack)
    for truckstatus in u_responses.truckstatus:
        t = threading.Thread(
            target = handle_truckstatus,
            args = (amazon_socket, world_socket, truckstatus))
        t.start()
    for error in u_responses.error:
        t = threading.Thread(
           target = handle_error,
           args = (amazon_socket, world_socket, error))
        t.start()

# Handle messages from amazon
def handle_amazon(amazon_socket, world_socket):
    global amazon_seqnum
    global world_seqnum
    
    # Read from amazon_socket
    # au_commands = recv_amazon(amazon_socket)
    au_commands = ups_amazon_pb2.AUCommands()
    au_commands = recv_msg(amazon_socket, au_commands)
    # dest_size = len(au_commands.dests)
    print(au_commands)
    for warehouse in au_commands.warehouses:
        t = threading.Thread(target = execute_gopickups, args = (amazon_socket, world_socket, warehouse, world_seqnum, ack_set))
        world_seqnum += 1
        t.start()
    for dest in au_commands.dests:
        truck_size = len(dest.leavingtrucks)
        t = threading.Thread(target = execute_godelivery, args = (amazon_socket, world_socket, dest, world_seqnum, amazon_seqnum, ack_set))
        world_seqnum += truck_size
        amazon_seqnum += truck_size
        t.start()

    for ack in au_commands.ack:
        print('Handle acks')

# Send world id to Amazon
def send_Amazon_worldid(worldid, seqnum):
    ua_commands = ups_amazon_pb2.UACommands()
    init_world = ua_commands.worlds.add()
    init_world.worldid = worldid
    init_world.seqnum = seqnum
    # settled = ua_commands.settled.add()
    # settled.packageid[:] = [10000]
    # settled.seqnum = 200
    print('init_world:\n')
    print(ua_commands)
    send_msg(amazon_socket, ua_commands)

    """
    # response = recv_msg(amazon_socket)
    au_commands = ups_amazon_pb2.AUCommands();
    au_commands = recv_msg(amazon_socket, au_commands)
    # au_commands.ParseFromString(response)
    print('ack:', au_commands)
    for ack in au_commands.ack:
        if ack == seqnum:
            break
    """
    
def main():
    global amazon_socket
    global world_socket
    global amazon_seqnum
    global world_seqnum
    
    # Get world id from user input
    worldid = input("Enter world id to connect or just hit enter to create a new one: ")
    if worldid and not worldid.isdigit():
        print("Error: world id should be digits.")
        return
    
    # Connect to World Server
    world_socket = connect_world_server()

    # Connect to world
    worldid, result = connect_world(world_socket, worldid, NUM_TRUCK_INIT)
    if result != 'connected!':
        print(result)
        return
    print(worldid, result)
    
    # Conenct to Amazon
    amazon_socket = connect_amazon()

    send_Amazon_worldid(worldid, amazon_seqnum)
    amazon_seqnum += 1
    
    # Repeatedly read from world or amazon
    inputs = [world_socket, amazon_socket]
    while True:
        # print('Before select')
        infds, outfds, errfds = select.select(inputs, [], [])
        # print('len(infds):', len(infds))
        if len(infds) != 0:
            for fds in infds:
                if fds is world_socket:
                    print('Received message from world')
                    handle_world(amazon_socket, world_socket)
                else:
                    print('Received message from Amazon')
                    handle_amazon(amazon_socket, world_socket)
        # print('After select')

    world_socket.close()
    amazon_socket.close()
    
if __name__ == "__main__":
    main()
