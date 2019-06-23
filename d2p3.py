# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:16:03 2019

@author: user
"""

# Here we write the client program for communicating with
# the server.
# The Psuedo code here
# Create a socket
# attempt to connect to the server
# while True:
#    input()
#    send()
#    receive()
#close()
#!/usr/bin/env python

from socket import *
# Address is the  same guy, connect to the server
# listening happening on port 21567 by d2p2

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
# Connect to the server
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    #send this in unicode format
    tcpCliSock.send(bytes(data, 'utf-8'))
    #receive from the same port
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        # He does not send anything 
        #close and tata/birla/bye-bye/astla-vitsa
        break
    # since the data is in bytes you need to decode
    print(data.decode('utf-8'))

tcpCliSock.close()
