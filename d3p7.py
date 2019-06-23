# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:18:51 2019

@author: user
"""

# What is ORM?
# Object Relational Mapping 
# Technique for storing, retrieving, updating and
# deleting in a relational database from an
# object oriented program
# There is a data layer that manages 
# the translation between the 2 concepts
# a library of classes and functions SQL alchemy
# is one such guy
# problems - inheritance , polymorphism
# rich class mapping are all issues
# each object roughly maps to a row
# Data layer - CRUD - saving
# pass an object to the data layer and
# that would insert a row
# Read
# when you select rows each row should get
# created as objects with constructors et al.
# Handling forieign keys and relationships become important
from sqlalchemy import Column,Integer, String, create_engine, exc, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# The engine in sql alchemy is the DB-API interface roughly for connnecting to 
# a database - this of it as the connection-- object
engine=create_engine("sqlite:///emp.db")
# Think of a session maker as a holding zone(buffer) for a connection that you make
# This class sessionmaker is now ready to execute transactions after binding it
# but will enter a transaction state i.e begin transaction for commits and rollback only when
# a query is executed as in session.query()
session= sessionmaker(bind=engine)()
# you can do session.commit() and session.rollback() after query execution
# Now what is this declaritive base
# This is the mapping of a table name to an object
Base=declarative_base()
# provides a bunch of table definitions from sqlite 
# I define a class called user and say that it inherits properties from base
# __tablename__ refers to the table that I am mapping this class to and and 
# the mapping columns to the columns of the class

class User(Base):
    __tablename__="rand"
    pk=Column(Integer, primary_key=True)
    n=Column(Integer)
    
    def __init__(self,pk,n):
        self.pk= pk
        self.n= n
user = User(84,10)
# This represents one instance of the class that is mapped to a row in 
# the database
session.add(user)
session.commit()
# session has a built in function called query
#I can construct a class mapped to a table
# pass that class to the session
# and query it for returning objects
result=[r.pk for r in session.query(User).all()]


# Please read this code and tell me what filter does
# Please state the parameter of filter
""" def update_state(chat_id, state):
    try:
        value = Users.query.filter(Users.chat_id == str(chat_id)).first()
        value.state = str(state)
        db.session.flush()
        db.session.commit()
        #db.session.close()
    except:
        print('Error in def update_state')
Once you have a set of valid objects retrieved you can commit
update is just changing values 
and delete is thru the delete
Read the code of d3p8 for a greater understanding of this. 
Focus on the update and delete functions
"""


