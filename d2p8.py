# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 08:21:27 2019

@author: user
"""

#ftpandsmail
#The ports at which ftp applications send and receive mail are usually
#FTP uses two TCP connections for communication. One to pass control information, 
#and is not used to send files on port 21, only control information. And the other, a data connection 
#on port 20 to send the data files between the client and the server. 
#The connection has to be established before the files can actually be sent across
# data is actaully sent over 20  and only login and othe such stuff is done over 21
# most download/upload ( except for torrents) happens using ftp
#Netflix uses the DASH (Dynamic Streaming over HTTP) protocol for streaming.
# to known what DASH means see https://youtu.be/nfjr_AbxogM
# Enough talking
#lets us get an some basic functions of ftp
#ftp hotname
#ftp login
#ftp ls
#ftp pwd
#ftp cwd
#ftp retr
#ftp get
#ftp put
#ftp quit/bye
#There is nothing more than than that in ftp
# So here is your exercise
 