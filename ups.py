import socket
import sys
import time
import psycopg2
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint
from proto import world_ups_pb2
from proto import ups_amazon_pb2
import build_commands
import ups_amazon_commands
import threading

# UPS_HOST = socket.gethostname()
# UPS_PORT = 54321
WORLD_HOST = 'vcm-9448.vm.duke.edu'
WORLD_PORT = 12345
AMAZON_HOST = ''
AMAZON_POST = ''

SEQNUM = 0;
NUM_TRUCK_INIT = 100

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
                database = 'wgzyjrdk',
                user = 'wgzyjrdk',
                password = 'NdCR_HW8uL-E-id_IUpNrn_cLNqEt593',
                host = 'isilo.db.elephantsql.com',
                port = '5432')
            # cur = dbconn.cursor()
            print('Successfully connected to the database')
            return dbconn
        except:
            print('Unable to connect to the database')
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
    u_connect = world_ups_pb2.UConnect()
    u_connect.isAmazon = False
    if world_id:
        u_connect.worldid = int(worldid)
        send_msg(world_socket, u_connect)
    else:
        for i in range(0, num_truck_init):
            trucks = u_connect.trucks.add()
            trucks.id = i
            trucks.x = 0
            trucks.y = 0
        send_msg(world_socket, u_connect)
        
    response = recv_msg(world_socket)
    u_connected = world_ups_pb2.UConnected()
    u_connected.ParseFromString(response)

    return u_connected.worldid, u_connected.result

# Receive UResponses from world
def recv_world(world_socket):
    response = recv_msg(world_socket)
    u_responses = world_ups_pb2.UResponses()
    u_responses.ParseFromString(response)
    return u_responses

# Receive AUCommands from Amazon
def recv_amazon(world_socket):
    response = recv_msg(world_socket)
    au_commands = ups_amazon_pb2.AUCommands()
    au_commands.ParseFromString(response)
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
    s.sendall(b"".join(hdr))
    s.sendall(msg.SerializeToString())

# Recv with encoded length info
def recv_msg(s):
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
    whole_message = s.recv(msg_len)
    return whole_message

# Handle messages from world
def handle_world(world_socket):
    # Read from world_socket
    u_response = recv_world(world_socket)
    for completion in u_responses.completions:
        handle_completion(completion)
        print('Handle completions')
        t = threading.Thread(target=f())
        t.start
    for delivered in u_responses.delivered:
        print('Handle delivered')
    for ack in u_responses.acks:
        print('Handle acks')
    for truckstatus in u_responses.truckstatus:
        print('Handle truckstatus')
    for error in u_responses.error:
        print('Handle error')
    # Do something...

# while True:

#     incoming = channel.recv( 100 )

#     if incoming: 
#         print "Received >%s<" % incoming
#         incoming = ''

def main():
    print('main() begins...')
    
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
    init_world = ups_amazon_pb2.InitWorld()
    init_world.worldid = worldid
    init_world.seqnum = SEQNUM
    SEQNUM += 1
    send_msg(amazon_socket, init_world)

    response = recv_msg(amazon_socket)
    au_commands = ups_amazon_pb2.AUCommands();
    au_commands.ParseFromString(response)
    for ack in au_commands.acks:
        if ack == init_world.seqnum:
            break

    # Repeatedly read from world or amazon
    inputs = [world_socket, amazon_socket]
    while True:
        infds, outfds, errfds = select.select(inputs, [], [])
        if len(infds) != 0:
            for fds in infds:
                if fds is world_socket:
                    # Read from world_socket
                    u_responses = recv_world(world_socket)
                    for completion in u_responses.completions:
                        # handle_completions()
                        print('Handle completions')
                        t = threading.Thread(target=f())
                        t.start
                    for delivered in u_responses.delivered:
                        print('Handle delivered')
                    for ack in u_responses.acks:
                        print('Handle acks')
                    for truckstatus in u_responses.truckstatus:
                        print('Handle truckstatus')
                    for error in u_responses.error:
                        print('Handle error')
                    # Do something...
                else:
                    # fds is amazon_socket
                    # Read from amazon_socket
                    au_commands = recv_amazon(world_socket)
                    for warehouse in au_commands.warehouses:
                        execute_gopickups(amazon_socket, world_socket, warehouse)
                    for dest in au_commands.dests:
                        execute_godelivery(amazon_socket, world_socket, dest)
                    for ack in au_commands.acks:
                        print('Handle acks')
                    # Do something...
    
    # Connect to database
    dbconn = connect_db()
    cur = dbconn.cursor()

    world_socket.close()
    cur.close()
    dbconn.close()
    
if __name__ == "__main__":
    main()
