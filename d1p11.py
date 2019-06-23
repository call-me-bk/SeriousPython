# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:18:36 2019

@author: user
"""

# Let us get iterators out of the way 
# you would have seen iterators when you 
# move thru lists
x = [1,2,3,4,5]
# to walk thru the list all we do is
# write a for loop like this
for i in x:
    print(i)
#i.e the variable i somehow keeps fetching
# new values till it reaches the end of the list
# makes it available to us.
# so it iterates thru the list
# so lets dig a little deeper
# let us try and do a deep dive into x
dir(x)
# it seems to have a method called iter
y=iter(x)
y
# This seems to be some object of type list_iterator
dir(y)
# This seems to have a method called next
y.__next__()
# So it gave me this first element in the list
y.__next__()
y.__next__()
y.__next__()
y.__next__()
# lets try one more
y.__next__()
# It ran out of objects and raised an exception
# to recap there is a built in class called list
# This hold a method called iter
# This method returns an object of type list iter
# This object has a method called next
# next keeps fething values from the object
# created from the list class till it runs out of values
# Psuedo code for doing iterators of a class
# Classs Myclass:
# some random object
# x = (1,2,3,4)
# __init__()
# def __iter__():
#   return object that we can traverse thru

 class RemoteControl():
     # all I have done is created a list 
         # and when remote is switched off it does
         # point to some online shoppin channel
    def __init__(self,list):
        self.channels = list
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]
my_play_list = ['Star Sports','Sony Six','Comedy Central', 'Colors Kannada']
r=RemoteControl(my_play_list)
for i in r:
    print(i)
my_play_tuple = ('Star SportsHD','Sony SixHD','Comedy CentralHD', 'Colors KannadaHD')
r=RemoteControl(my_play_tuple)
for i in r:
    print(i)
# There you go you have created a class 
# that is iterable for any iterable object
# the for loop does a couple of things
# it first executes the iter method 
# and gets the iter object
# it then executes the next method of the iter object
# The next method can do whatever it wants
# for example keep printing hello till som condition
# is met
class FaultyRemoteControl():
     # all I have done is created a list 
         # and when remote is switched off it does
         # point to some online shoppin channel
    def __init__(self):
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        return self.index
f= FaultyRemoteControl()
for i in f:
    print(i)
# Aste Iteratoru
        
        
        
         