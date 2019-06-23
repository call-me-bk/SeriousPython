# -*- coding: utf-8 -*-
"""
Created on Sat May 25 09:24:03 2019

@author: Srini
"""
# lists are just that that shopping lists
# and shopping lists change jargon mutable
# lists are enclosed in [] sqaure brackets
# lists can be nested - meaning lists within lists
list = []
print(list)
list.append("Ondu")
list.append(2)
print(list)
list.clear()
print(list)
list1 = [1,2,3,4]
list2 = [1,2,3,4]
list1.append(5)
list1.remove(4)
print(list1)
# what does insert do ? Insert at a particular position
list1.insert(3,4)
print(list1)
list1.insert(3,5)
list1 = [1, 2, 3, 5, 4, 4, 5]
#question - which element gets popped out 1 or 5 i.e fifo or lifo?
#question - what will the lsit look like after the pop - changed with 1 or 5 removed?
y = list1.pop()
print(y)
print(list1)
list1 = [1, 2, 3, 5, 4, 4]
# Question which of these elements get deleted
del list1[0:2]
print(list1)
# you can index a list
# print list[0] gives us the first elements
newlist = [ 1,'a','&','4']
# Let us visit our parser and see how this looks like
print(newlist[2])
newlist[2] = "Srini"
print(newlist[2])
# standard iterator for lists
for i in newlist:
    print(i)
dir(newlist)
# The newlist seems to have some function called __iter__
# Lets check this guy out - Ahem... I mean check ok?
newlist.__iter__()
# Some object it looks like because it is giving me an id?
# so why dont we assign it and inspect that object
y=newlist.__iter__()
dir(y)
# Ho Ho Ho - So we seem to have a method called __next__ which seems to do something
# newlist = [ 1,'a','&','4']
print(y.__next__())
# Once more please
print(y.__next__())
# So this is how this great for loop works right
# when you say
newlist = [ 1,'a','&','4']
for i in newlist:
    print(i)
# This is what it does 
# calls __iter__ of newlist and assigns it to something
# it then calls something.__next__ method of and 
# pushes the value to i
# lets examine this  to see if that indeed is true
# not clear enough right -
# Lets dig a little deeper
import dis
dis.dis('''newlist = [ 1,'a','&','4']
for i in newlist:
    print(i)''')
# We will spend day 4 on this code but trust me this is exactly 
# what this is doing - what you are seeing is the byte code in a
# readable format
# we will implement our own iterator by the end of today after defining a class
print(newlist[0:2]) # start from left and all upto right 
newlist = [ 1,'a','&','4']
dir(newlist)
# so what does __reversed__ do
print(newlist.__reversed__())
# gives me an object
newlist = [ 1,'a','&','4']
y = newlist.__reversed__()
dir(y)
# so this has a mehod called __next__
# show, show what this y.__next__()
y.__next__()
# so you get the idea that using the sign of the number given the slicer
# seems to call _reverse__ and then call __next__ in the iterator to 
# get the slice
newlist = [ 1,'a','&','4']
print(newlist[-1:])
print(newlist[:-1])
print(newlist[-2:-1])
newlist = newlist + [7,8,6]
print(newlist)
newlist= newlist.__add__(['a','b','c'])
newlist = [1,2]
newlist.__mul__(2)
# functionality like whet you have in matlab and numpy
# so maybe I can over ride these methods Right?
print(newlist)
newlist.remove('a')
# ok you can have list having lists and they have tuples and ..zzzzz
# tuples are immutable - means they cant change like the airtel girl
# who keeps saying that airtel if fastest, biggest - He He
nestedlist = [ 1, 2,3,4,5,6,(2,3,5)]
#try and print the nested elements in the sublist
for i in nestedlist:
    if isinstance(i,tuple):
        for j in i:
            print(j)
    else:
            print(i)
# The key here is not the loop - which all you guys know
# it is this inspector isinstance which tell you whether this is a list or
# on day 4 we quite extensively use this for code performance analysis
#tuples are like lists but cant change - immutable
tuple1 = (1,2,3,4)
print(tuple1[1])
print(len(tuple1),max(tuple1), min(tuple1))
#you can convert a tuple to a list and a list to a tuple
list1 = [ 1, 2,3,4]
t1 = tuple(list1)
print(t1)
# This is not an assignment - just some streches
#exercise 1 iterate thru a list of list, nonlist elements and give a count of 
lists, tuples, floats and strings
# give the total of all these number
x=[1,"2.14",3.14,[1,2,3],(3,3,3),[6,6,6]]
# exercise 2 change a tuple (1,2,3,4) to (1,2,"three","nalaku")

