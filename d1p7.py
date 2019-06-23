# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:09:51 2019

@author: user
"""
# large amoounts of this material is drawn from google's opensource python class
import re
match = re.search('esh','Ganesha')
#dont worry about what match is right now
#it has an function called group
#group return that matching string
try:
   x = match.group()
   print(x)
   # so if we dont find anything  we get an attribute error
except AttributeError:
    print('No matching String')
#Instead of typing this all over every single time let us write a function
#Remember group() returns the pattern found
def Find(pat,text):
    match = re.search(pat,text)
    if match:
        print(match.group())
    else:
        print('No matching String')
Find("esh","Ganesh")
#Rule 2 .(dot) matches any char except NEWLINE
#all of the char must be matched
#search goes from left to right
#stops as soon it finds it the first time
Find('..sh','Ganesha')
#how to find K.S in K.S.Srinivas 
Find('K\.S\.','K.S.Srinivas' )
#Remember the raw processing of Strings
#to Ensure that no special processing is done
#prefix the string with r
Find(r'K\.S\.','K.S.Srinivas' )
#Rule 3 \w matches word a-z,0-9,_
#\w is a word character of the above type only
Find(r'\w\wMushika','::Mushika')
Find(r'\w\wMushika','__Mushika')
#Rule 4 \d matches only digits
#Rule 5 \s matches for space , tab
Find(r'\d\dMushika','__Mushika')
Find(r'\d\dMushika','21Mushika')
#matches the 2 whitespaces in Mushika
Find(r'\s\sMushika','  Mushika')
#_____________________________________
#
# a + means one or more of the post char
# a * means zero or more of the post char(succeeding character)
#
# so the above line could have been written as
Find(r'\s+Mushika\s*Vahanam','    Mushika Vahanam') # 3 sp
Find(r'\s+Mushika\s*Vahanam','    MushikaVahanam')
# left and largest
#Rule 6 \S means all non-whitespace characters
Find(r'OM\S+','Song of OMGanesha-Shankar_Eshan$Loy* sung at')
#Let us try and extract an email 'srinivas.katharguppe@gmail.com'
#for this we need to look at  another pattern [] meaning anything in this set
Find(r'[\.\w]*@[\.\w]*','bbb srinivas.katharguppe@gmail.com  ...')
Find(r'[\.\w-]*@[\.\w]*','bbb srinivas.kathar-guppe@gmail.com ...')
Find(r'[\.\S]*@[\.\S]*','bbb srinivas.kathar-guppe@gmail.com  ...')
