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
PORT1 = 22222
PORT2 = 22221
BUFSIZ = 1024
ADDR1 = (HOST, PORT1)
ADDR2 = (HOST, PORT2)

udpSerSock1 = socket(AF_INET, SOCK_DGRAM)
udpSerSock1.bind(ADDR1)

udpSerSock2 = socket(AF_INET, SOCK_DGRAM)
udpSerSock2.bind(ADDR2)

# No Accept
# Also note there is no outer while loop
while True:
    print('waiting for message...')
    data1, addr1 = udpSerSock1.recvfrom(BUFSIZ)
    data2, addr2 = udpSerSock2.recvfrom(BUFSIZ)
    
    #if data1:
    udpSerSock2.sendto(bytes('[%s] %s' % (ctime(), data2.decode('utf-8')), 'utf-8'),addr1)
    
    
    #elif data2:
    udpSerSock1.sendto(bytes('[%s] %s' % (ctime(), data1.decode('utf-8')), 'utf-8'),addr2)
    
    #else: continue
    #udpSerSock.sendto('[%s] %s' % (ctime(), data.decode('utf-8')), addr)
    print('...received from and returned to:', addr1)
    print('...received from and returned to:', addr2)
udpSerSock1.close()
udpSerSock2.close()