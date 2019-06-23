# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:15:11 2019

@author: user
"""

from mydb import MyDB
import pytest
# There are expensive operations like connections to
# database that when performed lead to overheads
# Let us look at this example
"""def test_johns_id():
    db = MyDB() # instance of the class of MDB
    conn = db.connect("127.0.0.1")
    cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123
def test_toms_id():
    db = MyDB() # instance of the class of MDB
    conn = db.connect("127.0.0.1")
    cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=tom")
    assert id == 789"""
# So what is the problem here
# you can see that 14-16 and 20-22 are repeated
# Thats an expensive operations
# Jusst you would use a car jack to fix your car tyre change
# we similarly use a fixture out here
#-------------------------------------
# New way of doing things
@pytest.fixture()
# the statement below sets up the fixture only once 
#@pytest.fixture(scope="module")
def cur():
    print("Setting up")
    db = MyDB() # instance of the class of MDB
    conn = db.connect("127.0.0.1")
    curs = conn.cursor()
    return curs
    # when we need to do a tear down
    # change return to yield curs
    # curs.close()
    # conn.close()
    # These would ensure that the connection pool gets back stuff
def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123
def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789
# what this does is avoid code duplication
# Run this with the --capture=no
# You can see that this fixture is being setup twice
# In order to prevent that you state scope="module"
# Now how do 

    