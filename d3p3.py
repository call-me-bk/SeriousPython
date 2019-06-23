# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:03:50 2019

@author: user
"""

# lambda - These are anonymous functions
def square(a):
    return a*a
f= lambda a:a*a
print(square(5))
print(f(6))

# dont seem to be of great use right
# Lets see in the next example

# let us get the other guy out of the way 
# partial functions are function created on top of function with parameters half filled
# EXAMPLE
def func(a,b,c,d):
    x=a+b+c+d
    return x
    # whatever that means
# Now this supecomplex function has under certain conditions a=1,b=2,c=4 which only d changing
from functools import partial as pto
# I can now define a new func easy_func with these parameters fixed
easy_func=pto(func,1,2,4)
print(func(1,2,3,4))
print(easy_func(3))
# thats all boss nothing extra ordinary
# BUT WHY THESE TWO CONCEPTS RANDOMLY IN THE MIDDLE OF SOMETHING
# The next example will help you understand and thene maybe we do a bit of functional programming
# and iterators and generators and this new thing calles ups from the apc standard
    