# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:30:18 2019

@author: user
"""

# Here is the psuedo code for the UDP Server
# write the code for  this
# ss = socket()
# ss.bind()
# while True:
#   cs=ss.recv()
#   ss.sendto()
#close()
#!/usr/bin/env python


from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
# No Accept
# Also note there is no outer while loop
while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'),addr)
    #udpSerSock.sendto('[%s] %s' % (ctime(), data.decode('utf-8')), addr)
    print('...received from and returned to:', addr)

udpSerSock.close()
