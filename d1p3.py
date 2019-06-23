# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:08:55 2019

@author: user
"""

# exception handling is important
# standard suspects are div by zero, io error
try:
    x = 1
    y = 0
    x/y
except ZeroDivisionError:
    print("Divide by Zero ! Huh")
# What do you get when you try to add Srini ti a complex number
# type error offcourse , because Srini is not a complex guy
x = "Srini"
try:
    y = 2 + 2j
    p = x + y
    #print(p)
except TypeError:
    print("mismatch in your type")
# and a exception to catch all situations
try:
   x = "Srini"
   y = 2 + 2j
   x/y
   print("hello world")
except ZeroDivisionError:
    print("Divide by Zero ! Huh")
except:
    print("Will catch all other errors")
finally:
    print("Will exceute no matter what")
# Exercise try and find the type of error that happens programmatically
# example x="rama" y="zero" and x/y , print the error
# This is a type error because Allah/Rama/Christ can never be Zero
try:
    x="Rama"
    y="Zero"
    x/y
except Exception as ex:
    print(type(ex).__name__)
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
# how can we raise exceptions programmatically and defining custom exceptions
# I can define my own custome exceptions
# By inheriting a class of type exception
class CustomException(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        # repr only does a string  representation of the object
        return repr(self.parameter)
try:
    raise CustomException("My Useful Error Message")
except CustomException as ex :
    print(type(ex).__name__)
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
    print ("Caught: custom exception")
# Dukan Bandh ... Picture to bake hey 

