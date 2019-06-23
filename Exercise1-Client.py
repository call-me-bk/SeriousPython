# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:37:28 2019

@author: user
"""

#!/usr/bin/env python
"""
# Here is the Psuedo code for the client
cs = socket() # create client socket
comm_loop: # communication loop
cs.sendto()/cs.recvfrom() # dialog (send/receive)
cs.close() # close client socket
"""

from socket import *
from time import ctime
HOST = '127.0.0.1'
PORT1 = 22222
PORT2 = 22221
BUFSIZ = 1024
ADDR1 = (HOST, PORT1)
ADDR2 = (HOST, PORT2)
user = [ADDR1, ADDR2]

x = int(input("Enter user1 or 2: " ))
ADDR = user[x-1]
udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(bytes(data, 'utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

udpCliSock.close()
