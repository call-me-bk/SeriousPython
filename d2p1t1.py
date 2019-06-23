# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:15:07 2019

@author: user
"""

# Let us do networks on day 2
# A little bit of theory to fill you up
# Client - any piece of hardware or software requesting for something
# Server - any h/w or s/w responding to a request
# Servers are a little different Like they wait forever to respond to clients
# Psuedo code would be 
# while True:
#   accept a request()
#   open_connection()
#   while connection_exists():
#       receive()
#       respond()
#   close_connection()
# Much like an ATM waiting for you to insert the card
# accept card
# ask what you want to do
# fulfill it 
# when you say thank you
# close the card and blink
# wait for another card
# example are webserevr, databaseserver, fileserver
# client needs to something far more simple
# Psuedo code for client would be
# get_the-server_addr()
# request_connection()
# while connected
#   send_rqeuest()
#   get_responses()
#close_connection()
# for two people to talk to each other there must be a communication channel
# Think of this as a cable between client and server
# now the channel exists but does not have end points but unconnected
# What do we call the end point of an electrical wire - 
# yup a socket one to the transformer the other to your plug point
# so both clients and servers need to have communication end points called sockets
# enough of this theory time for a little break
# lets say your laptop is the client - I need a name or as in networks a IP address
# how do you find the IP of your machine in python
import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(hostname)
print(ip)
ip=socket.gethostbyname('www.google.com')
print(ip)
# do a ipconfig or an ifconfig and see your hostname
# now you want to connect to google using http
# let us not worry about what http meands now
# how to find google's p address
# this guy called socket is the end point
# Google is a big guy, he has many people listening for him - someone doing mails, someone doing maps, some
# doing googleing - serach - but each guy is listening in the same place in a different port hole
# so the socket = end point means = ipaddress+ some port hole
# each of the different types of applications listen to different port(logical) holes
# try googling and find the ports for ftp,email(SMTP) + Surf(HTTP)
# the socket seems to be made of 2 parts like your house address and your name in a letter
# Srini = your name = geekese = port number
# PSR, Bsk = youd address = ipaddress
# and for a socket to actually work well we need both your name and the address
# now you need to know what language is this address writtern in i.e the address format
# is it IPv4 32 bits or 128 bits potentially connection every cooker, sweater and pen
# We also have connection oriented and connection less protocols
# you should also tell the socket whether it needs to behave like a normal post or registered post
# meaning normal post may get delivered , registered post theorrically should get delivered
# so you have packets that can get split, retransmitted and even check for duplicates
# your normal post is fast but not free from error = UDP
# your registered post is a little slower but has far lesser errors = TCP
# so you need to tell your socket speed or safe, type of address and finally whom are you sending to
# socket comprises of host ip, port number, type of transmission tcp or udp
# you listen to port 80 HTTP program
# your mother listends to port 21 FTP Program
# Dad listens to 25 SMTP programs
# Spoiler alert - one ip/port combination can be listened to by one program
# no sharing of ear plugs here
# socket takes two important paremeters
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  This is is a data structure with some methods
# AF_INET means use ipv4 addresses
s2 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
# means use ipv6 addresses
# SOCK_STREAM means use TCP
# SOCK_DGRAM means use UDP
s3 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
# proto =0 except for some AF_CAN ; have not used it
# All theory over now some code 
