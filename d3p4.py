# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:48:10 2019

@author: user
"""

# To get talk to a db but whatever means , we need an API
# what better name than to call it DB-API . Current version is 2.0
# It must specify apilevel, thread safety, exception
# and a very important connect function()
# it is critical that we undersatnd this connect function
# This connect function is made avaiable thru an object and returns a connection
# object
"""
user Username
password Password
host Hostname
database Database name
dsn Data source name""" 
# These parameters are passed as
# connect(dsn='myhost:MYDB',user='user1',password='password')
# Randon fact did you know that password is one of the most common passwords
"""
close() Close database connection
commit() Commit current transaction
rollback() Cancel current transaction
cursor() Create (and return) a cursor or cursor-like object
using this connection
errorhandler(cxn, cur,
errcls, errval)
Serves as a handler for given connection cursor
"""

# we seem to understand close(), commit() and rollback()
# but what is a cursor
# The cursor method returns a cursor object which has many methods
# such as execute('sql command')
# fetch a set of rows using fetchone(), fetchall()
# Also we often need to change the values to certain object
# type specified such varchar, binary, blob etc 
# ENough lets run a program and see this in action
