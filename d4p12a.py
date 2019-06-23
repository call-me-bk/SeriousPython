# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:16:56 2019

@author: user
"""
dict = {1:'Ganesh',2:'Srini'}
dict1 = {11:'Ganesh',12:'Srini'}
def One(dict,key):
    try:
        print(dict[key])
    except KeyError:
        print("Error")
One(dict,1)
One(dict1,1)

# Why try catch at all
def Ondu(dict,key):
    if 1 in dict:
        print(dict[key])
# replace the print with a return if you want to make this meaningful
x=Ondu(dict,1)
x=Ondu(dict1,1)
if x:
    print("hello")
else:
    print("Not There")

# But exception raises a stack call
# why not use the GET method of dict

def ek(dict,key):
    print(dict.get(key),"Yaru Ella")
ek(dict,1)
ek(dict1,1)

# Much more elegant, and default returned
# Lets take some sets
my_set = {1,2,4,5}
def set_catch(mset,val):
    for i in mset:
        if i != val :
            print("Not there")
        else:
            print("3 found")
set_catch(my_set,3)
#my_set.add(3)
#set_catch(my_set,3)
def set_catch1(mset,val):
    if bool(mset.intersection(set([val]))):
        print("3 Found")
    else:
        print("Not There")
set_catch1(my_set,3)
# What do think is more efficient
# Let us look at the profiler next
#let us create an simple d4p14
    

        

