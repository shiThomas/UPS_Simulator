#! /usr/bin/python3

import socket, select
import sys

host = 'vcm-9448.vm.duke.edu'
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.sendall(b"Hello, I'm 7992")

while True:
    data = input("Enter input: ")
    s.sendall(b"7992")

s.close()

"""
inout = [socket]

while True:
        infds, outfds, errfds = select.select(inout, inout, [], 5)
        if len(infds) != 0:
                buf = socket.recv(1024)
                if len(buf) != 0:
                        print 'receive data:', buf
        if len(outfds) != 0:
                socket.send("python select client from Debian.\n")
"""
