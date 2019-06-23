# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:43:51 2019

@author: user
"""

# ok last topic on performance
import dis
abc = ('a', 'b', 'c')
def concat_a_1():
    for letter in abc:
        abc[0]+letter
def concat_a_11():
    for letter in abc:
        a+letter
dis.dis(concat_a_1)
print("Seperator")
dis.dis(concat_a_11)
def x():
    return 42
dis.dis(x)
def x1():
    def y():
        return 42
    return y()
dis.dis(x1)
# see the number of extra opcodes that you need to 
# perform before the same 42 is returned
# very useful functionality
# Let us introspect a little 
# we have being doing this for a while now
