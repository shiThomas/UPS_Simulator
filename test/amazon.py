#! /usr/bin/python3

import socket
import sys
import time
import psycopg2
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint
from proto import world_ups_pb2
from proto import world_amazon_pb2
from proto import ups_amazon_pb2

HOST = socket.gethostname()
PORT = 12345

WORLD_HOST = 'vcm-9229.vm.duke.edu'
WORLD_PORT = 23456


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
def connect_world(world_socket, worldid):
    a_connect = world_amazon_pb2.AConnect()
    a_connect.isAmazon = True
    a_connect.worldid = worldid
    send_msg(world_socket, a_connect)

    response = recv_msg(world_socket)
    a_connected = world_amazon_pb2.AConnected()
    a_connected.ParseFromString(response)

    return a_connected.worldid, a_connected.result

# Send with encoded length info
def send_msg(s, msg):
    hdr = []
    _EncodeVarint(hdr.append, len(msg.SerializeToString()), None)
    s.sendall(b"".join(hdr))
    s.sendall(msg.SerializeToString())

def main():
    print('starting')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print('starting')
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        var_int_buff = []
        while True:
            buf = conn.recv(1)
            var_int_buff += buf
            msg_len, new_pos = _DecodeVarint32(var_int_buff, 0)
            if new_pos != 0:
                break
        whole_message = conn.recv(msg_len)
        print(whole_message)

        # conn.sendall(data)
        # u_connect = world_ups_pb2.UConnect()
        # u_connect.ParseFromString(whole_message)
        # print(u_connect)

        ua_commands = ups_amazon_pb2.UACommands()
        ua_commands.ParseFromString(whole_message)
        print(ua_commands)

        for init_world in ua_commands.worlds:
            world_socket = connect_world_server()
            worldid, result = connect_world(world_socket, init_world.worldid)

            print(result)
            break

        msg = ups_amazon_pb2.AUCommands()
        warehouse = msg.warehouses.add()
        warehouse.whid = 1
        warehouse.wh_x = 5
        warehouse.wh_y = 6
        warehouse.seqnum = 1
        package = warehouse.packageinfos.add()
        package.description = 'description'
        package.count = 10
        package.packageid = 1
        package.x = 10
        package.y = 20
        package.upsaccount = 'user'

        send_msg(conn, msg)
        while True:
            print('Connected by', addr)
            var_int_buff = []
            while True:
                buf = conn.recv(1)
                var_int_buff += buf
                msg_len, new_pos = _DecodeVarint32(var_int_buff, 0)
                if new_pos != 0:
                    break
            whole_message = conn.recv(msg_len)
            print(whole_message)

            # conn.sendall(data)
            # u_connect = world_ups_pb2.UConnect()
            # u_connect.ParseFromString(whole_message)
            # print(u_connect)

            ua_commands = ups_amazon_pb2.UACommands()
            ua_commands.ParseFromString(whole_message)
            print(ua_commands)

        conn.close()
if __name__ == "__main__":
    main()
