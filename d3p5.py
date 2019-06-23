# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:46:46 2019

@author: user
"""

import os
import sqlite3
# Returns a connection object when you connect
cxn=sqlite3.connect("example.db")
# as Mentioned before the connection object can commit, rollback, fetch,
# execute as functio
dir(cxn)
cur=cxn.cursor()
cur.execute('create table tbl1 (name char(20), age integer)')
cxn.execute('create table tbl (name char(20), age integer)')
cxn.execute('insert into tbl values ("Srini",54)')
cxn.execute('insert into tbl values ("Ganesh",21)')
# This returns a cursor which we dont need just yet
# Let us insert a few more records
cxn.commit()
# now we need a cursor object to contain all the rows
cur= cxn.execute("select * from tbl")
for i in cur:
    print(i)
# seems to return tuples right one for each row
cur= cxn.execute("select * from tbl")
dir(cur)
cur.fetchone()

for i in range(20):
    cxn.execute('insert into tbl values( %s,%d)' %(str(i), i))
cur= cxn.execute("select * from tbl")
for i in cur:
    print(i)
cxn.rollback()
cur= cxn.execute("select * from tbl")
for i in cur:
    print(i)
