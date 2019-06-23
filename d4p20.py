# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 06:57:02 2019

@author: user
"""

import sys
b = sys.intern("A Really long string")
a = sys.intern("A Really long string")
print(b is a)
c="A Really long string"
print(c is a)

def func():
    str = "String"
    id = 10
    print(id*' ',str)
func()
func.__code__
func.__code__.co_consts
# You can see that there are 4 constants that seem to be stored
# Which do you think is faster
key="pk2"
my_set = {"pk1", "pk2","pk3"}
if key in my_set: print("True")
# This is a constant cost operation .
def func1():
    key="pk2"
    pk = "pk99"
    my_set = {"pk1", "pk2","pk3"}
    if key in my_set: print("True")
    my_list = ["pk97", "pk99","pk98"]
    if pk in my_list: print("True")
func1.__code__.co_consts
# You can see that both these are store in are treated as constant cached in memory
# and therefor faster

