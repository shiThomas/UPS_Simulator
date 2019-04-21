import socket
import sys
import time
import psycopg2
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint
from proto import world_ups_pb2


# UPS_HOST = socket.gethostname()
# UPS_PORT = 54321
WORLD_HOST = 'vcm-9448.vm.duke.edu'
WORLD_PORT = 12345
AMAZON_HOST = ''
AMAZON_POST = ''

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
                user='wgzyjrdk',
                password='NdCR_HW8uL-E-id_IUpNrn_cLNqEt593',
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
            print('Successfully connected to World')
            return world_socket
        except:
            print('Unable to connect to World')
            continue

# Connect to World or create a new World
def connect_world(world_socket, world_id):
    u_connect = world_ups_pb2.UConnect()
    if world_id:
        u_connect.worldid = int(world_id)
    u_connect.isAmazon = False
    send_msg(world_socket, u_connect.SerializeToString())
    # print(u_connect.SerializeToString())
        
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
    _EncodeVarint(s.send, len(msg), None)
    s.send(msg)

# Recv with encoded length info
def recv_msg(s):
    var_int_buff = []
    """
    while True:
        buf = s.recv(1)
        var_int_buff += buf
        msg_len, new_pos = _DecodeVarint32(var_int_buff, 0)
        if new_pos != 0:
            break
    """
    whole_message = s.recv(1024)
    print(whole_message)
    u_connect = world_ups_pb2.UConnect()
    u_connect.ParseFromString(whole_message)
    print(u_connect)
    return whole_message

# while True:

#     incoming = channel.recv( 100 )

#     if incoming: 
#         print "Received >%s<" % incoming
#         incoming = ''

def main():
    print('main() begins...')

    world_id = input("Enter world id to connect or just hit enter to create a new one: ")

    if world_id and not world_id.isdisit():
        print("The world id should be digits.")
        return

    # Connect to World
    world_socket = connect_world_server()
    
    connect_world(world_socket, world_id)

    response = recv_msg(world_socket)

    u_connect = world_ups_pb2.UConnect()
    u_connect.ParseFromString(response)
    print(u_connect)

    # Connect to database
    dbconn = connect_db()
    cur = dbconn.cursor()

    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print('db_version is:\n', db_version)

    cur.close()
    dbconn.close()
    
if __name__ == "__main__":
    main()
