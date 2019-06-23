# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:05:26 2019

@author: Srini
"""
# A few simple concepts every database is like your excel workbook
# each workbook contains many worksheet. Each of these work sheets 
# can be thought of as tables. Each worksheet will have different columns to 
# represent different data values. These are your columns and each row is
# what else a  row in a sheet
# So we create a database similar to an xls file to store related tables using
# the create database command in RDBMS. R stands for relations and not ... 
# Locate your sqllite3.exe file or whatever your executable is called and run it
# you should see a sqlite> prompt
# Here type .open employee;
# The standard database has create database dbname ; and then a bunch of options
# To find all the tables ( sheets) in your database type .tables
# None as of now . Now create tables like reptiles, mammals to store different animals
# create table reptile ( animal_id integer, animal_name char(40), location char(10));
# so we now have a sheet with different columns called animal_id, animal_name and location 
# of different datatypes
# should we not have all animals have an a unique id like Tagging them; In US they havs SSN and we have Aadhar
# These are called keys
# forget animals let us look at employees
# what do you think the following statement will do
"""CREATE TABLE employees
( employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
  last_name CHAR NOT NULL,
  first_name VARCHAR,
  hire_date DATE
);"""
# Several new things here primary key means that every row( record ) can contain
# unique value is this column
# autoincrement means that these get autoincrement everytime you create a row
# there are other data types such a varchar larger amounts of char, date 
# and another constraint called not null. Means you cant leave it empty
# INSERT INTO table_name VALUES (value1, value2, value3,...);
# table_name: name of the table.
# value1, value2,.. : value of first column, second column,... for the new record
# try inserting duplicate records, records where columns are to be not null and see what happens
# to insert only certain columns here is the syntax
# INSERT INTO table_name (column1, column2, column3,..) VALUES ( value1, value2, value3,..);
# a few more commannds and then we are all set
# SELECT column1,column2 FROM table_name WHERE Column1="literal" AND column2="Literal";
# UPDATE table_name SET column1 = value1, column2 = value2,... 
# WHERE condition;
# and finally actually not finally 19th over 
# DELETE FROM table_name WHERE some_condition;
# DROP TABLE table_name; - deletes the table and its rows
# except for drop and create - so called ddlj other statements can be roflled(aka rolled) back
# or you can make it permanent by saying commit means that you can no longer do late nights
# enough theory
# practice these on sqlite3.
# create a database called spbatch1.db
# create a table called registered_learners with the following 
# columns ( id int primary key autoincrement, name char(20), score int, doj date)
# add a few students into the table
# get the names and ids of all students who have scored more than 50 whose name starts with sri
# delete these guys
# exit sqlite3 and come back and see these students
# if these students the sri and > 50 are there delete them and commit
# drop the table 
# .open dbname
# .databases
# .tables
# create table registered_student ( id integer primary key autoincrement, 
# name varchar(20));
# .tables
# insert into registered_student values (1,"Srini");
# .dump registered_student
# select * from registered_student;
#INSERT INTO registered_student VALUES(1,'Srinivas');
#INSERT INTO registered_student(name) VALUES('Srinivas');
# update registered_student set  name = 'srini' where id=2;
# select * from registered_student;
# delete from registered_student where name='srini' and id=1;
# select * from registered_student;
# delete from registered_student where name like'%ri%;
# .schema sqlite_master
""" CREATE TABLE sqlite_master (
  type text,
  name text,
  tbl_name text,
  rootpage integer,
  sql text
"""
# select * from sqlite_master;
# ok you now know that we can extract table names, we can also extract sequences(autoincrements), indexes , clusters etc 
# remember this - it will be useful as we go thru the exercises of day3
