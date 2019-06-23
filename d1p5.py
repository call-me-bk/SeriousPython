# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:18:37 2019

@author: user
"""
# Sets are an unordered collection of hashable
# means no duplicates.
# They  must be immutable members
# A set object is an unordered collection of distinct hashable objects. 
#Common uses include membership testing, removing duplicates from a sequence, and 
#computing mathematical operations such 
# as intersection, union, difference, and symmetric difference.
# exercise try a create a set of tuples, lists, sets and after this exercise set of sets- whet ever that mean

normal_set = set(["ka","kha","gha","ga","na","a","b"])
print(normal_set)
print(len(normal_set))
normal_set.add("cha")
print(normal_set)
normal_set.add("cha")
print(normal_set)
normal_set.remove("cha")
normal_set1 = {"a","b","c","d"}
n
normal_set.union(normal_set1)
normal_set.intersection(normal_set1)
# Remember these operations - These are extermely well implemented and can 
# save many operations as opposed to iterations - written as c module
ns1 = frozenset(["a","b","c"])
#ns.add("d") 
ns2 = {"d","e","f",ns1}
# Dictionary are implemented as hash table
# so whats a hash table
#
#
#
#
# dictionaries are key value pairs
x = {1:"Ek",2:"Yeradu",3:"Three"}
x[1]
x.keys()
x.get(2)
x[2]="do"
x.values()
# -*- coding: utf-8 -*-
#create a dictionary with a key value pair
dict = {'tim':18,'charlie':12,'tiffany':22}
#find  a key
print(dict['tim'])
#add an element into into the dictionary
dict.update({'mom':49})
print(dict.get('tim'))
#dict.clear() # clears all elements in dictionary
pick = {'mime':18, 'mp4':46}
# update dictionary by adding elements with another dictionary
dict.update(pick)
pack = pick.copy()
print(pack.items())
# a dictionary can also have tuples as elements
# given this try and create an dictionary that has the following
# key is some role number and a tuple of tuples with subject and marks
# example key= srini, "chem=45, phy=50,math=50,bio=46" and then given a name and subject pair print the marks
# for getting values from the screen you can use input
# clue given here in the next example
# some databases use this concept
x=input()
# raw input not recommended
rec = {'pk1':('Sreedhar', 60, 'retired'), 'pk2':('Abhoshek',40,'lossy')}
#dictionary can have tuples, other dictionaries , recursive elements into the 
# the value part
tup = rec['pk2']
for i in tup:
    print(i)
# do you think you could create a database with this example
