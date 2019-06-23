# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:39:02 2019

@author: user
"""

# for any client server program
# you need to create a server
# The psuedo code is 
# socket() - create a socket
# i.e say what ip type and what transport type
# bind() - connect the socket to an IP and port
# listen() - wait for requests to come in
# while True:
# accept() - accept request from clients
#   while no-more_request()
#       receive() - receove message()
#       send() - send responses
#   close() - close the client
# close() the connection
#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
# you can use 127.0.0.1 - local host
PORT = 21567
#  Lower ports numbers are occupied so use so number over 9999
BUFSIZ = 1024
# read in sizes of 1024 byts
ADDR = (HOST, PORT)
# a socket needs your name and your address
# i.e use your IP address and port number

tcpSerSock = socket(AF_INET, SOCK_STREAM)
# We are creating a TCP socket so SOCK_STREAM
# I am using ipv4 addresses so use AddressFamily_INET
# Plug the address, port pair to the socket which has 220v/50hz i.e TCP and IP4 addresses
tcpSerSock.bind(ADDR)
# Start listening - accept upto 5 connections at a time
tcpSerSock.listen(5)
#### Trial not sure - remove if this bombs
## data=bytes()
while True:
    print('waiting for connection...')
    # This is blocking type connection
    # wait till someone wants to talk to you
    tcpCliSock, addr = tcpSerSock.accept()
    print(addr)
    print(tcpCliSock)
    # when the other guy talks accept it and note
    # his addr and the socket from which he connected
    print('...connected from:', addr)
    # Now start waiting for his request
    while True:
        #receive data upto 1024 bytes at a time
        data = tcpCliSock.recv(BUFSIZ)
        print(data)
        if not data:
            break
        #tcpCliSock.send('[%s] %s' % (bytes(ctime(),'utf-8'), data))
       # Send his data back with a time stamp
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))
    # if he does not send anything close
    tcpCliSock.close()
#bring down the server
#try this if shutdown is given then bring the server done
#never done in real life but just an example
    
tcpSerSock.close()
# go to your command prompt and in the location type
# python d2p2.py
# Server is up an running

