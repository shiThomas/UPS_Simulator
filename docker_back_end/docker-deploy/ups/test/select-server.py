#! /usr/bin/python3

import socket, select

host = gethostname()
port = 10000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
socket.listen(5)
inputs = [socket]

while True:
    infds, outfds, errfds = select.select(inputs, [], [], 5)
    if len(infds) != 0:
        # print('enter infds')    
        for fds in infds:
            if fds is socket:
                clientsock, clientaddr = fds.accept()
                inputs.append(clientsock)
                # print('connect from:', clientaddr)
            else:
                # print('enter data recv')
                data = fds.recv(1024)
                
                if not data:
                    inputs.remove(fds)
                else:
                    print(data)

    """
    if len(outfds) != 0:
        # print('enter outfds')
        for fds in outfds:
            fds.send("python select server from Debian.\n")
    """
