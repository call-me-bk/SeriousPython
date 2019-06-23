# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:25:23 2019

@author: user
"""


# The bahubali of python, kattappa introduced soon
# String and string processing 
s1 = "String"
s2 = 'String'
s3 = ''' really long string which can span 
multiple lines'''
s4 = """really long string which can span 
multiple lines"""
print(s1,s2,s3,s4,s1+s2+s3+s4)
s5 = 'can \t contin tabs and \n as well'
print(s5)
longstring ="PES University Summer Course Serious Python"
# Nice tokenizer that can be used for writing simple parsers, like the ast
x = longstring.split()

for i in x:
    print(i)
print(x)
#can include unicode characters
# prefic u for unicode, r for raw strings etc
print(u"\u0041")  # A
print(u"\U0001F601")  # 😁
print(len(longstring))
s6 = r'can \t contin tabs and \n as well'
print(s6)
s7 = 'can \\t contin tabs and \n as well'
print(s7)
fourth = s4[3:4] # should give us a
print(fourth)
# There is a whole module this afternoon on strings 
# trailer of the movie called regex
import regex as re
