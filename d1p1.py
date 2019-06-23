# -*- coding: utf-8 -*-
"""
Created on Sat May 25 08:22:57 2019

@author: Srini
"""
# this is a single line comments
# Technically there are no multi line comments i.e /* ... */
# """ are technically not comments but multiline
# strings
x = """ multiline line string that
spans lines """
# Question 1: what is the length of a long string in python? 
print(x)
# Guido recommends using # in all line for comments
#variables dont have to declared and are inferred
# variable are labels and are mutable
# Variables dont exist in python - they are actually labels for a target 
# instruction to pointing to a memory location
x = 10
print(x)
x = "CGPA"
print(x)
# 4 number types
# Integers
i = 1
i1 = -3
i2 = 99999999
i3 = -9999999
# Question 2: How do you find the sign of an integer
# Tip : Most of these questions have some significance - wink, wink
# Let us try and find what is i
type(i)
dir(i)
i.real
# Looks like i is some kind of an object of type int and has some methods
print(i.__add__(2))
print(i.__sizeof__())
# Question : what is this 28 , We all known that the size of int is generally 24
# bytes
import sys
sys.getsizeof(i)
print(i,i1,i2,i3,i+i1+i2+i3)
#floats
f = 1.0
f1 = -1.5
f2 = 10e5
f3 = -10e5
f4 = -10e-5
print(f, f1,f2,f3,f4,f+f1+f4)
#complex numbers 
c = 3 +2j
c1 = -4 + 2j
# you know how to multiply complex numbers right FOIL
print(c+c1)
# Reals get added to the real and imag gets added to imaginary
x = i + f + c
print(x)
# booleans are true or false
t = True

t1 = true
print(t, t1) # true is not defined
t2 = True
y = 1 + t2 
print(y)
f0 = False
y = 1 + f0
print(y)
# so booleans are for arithmetic 1 and 0
# lets get some operators
 y = 3
 x = 2
 print(y/x)
 print(y//x)
 print(y%x)
y = 3.0
x = 2.0
print(y/x)
print(y//x)
print(y%x)
y=3
x=2.0
print(y%x)
# moral of the story / div // integer div % modulus
# lets wrap up numbers with these
m = 2 + 2j
n = 3 + 3j
p= m**n
print(p)
# https://math.stackexchange.com/questions/476968/complex-power-of-a-complex-number
#
print(m.real, m.imag)
import math
i=1
f1 = 1.5
c = 2 + 2j
a = i + int(f1)
# b = float(c) # cant do this
print(a) 
print(round(f1))
print(math.ceil(f1))
print(math.floor(f1))
a=2
b=3
c=a+b
# https://vpyast.appspot.com/
42
type(a)
dir(a)
a.__add__(2)
# so there is a function called _add__ which seems to add values
# These dir and type are used for introspections or inspecting the values
# more on that later
# Question? so are there pointers in python and can I find the value of the address
a=1
id(a)
# seems to give me some unique object identifier
import ctypes
# Certain implementations such cpython can catually give you the address
# but...
a = [1,2,3,4]
b= []
b=a
print(id(a))
print(id(b))
b.append(5)
print(a)
# So some kind of pointer mechanism seems to be working

