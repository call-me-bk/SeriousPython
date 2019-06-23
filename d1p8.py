# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:54:42 2019

@author: user
"""

#Let us stop using our Find function
import re
#we used re.search to return a match object
#we used group function to return what we found
# Let us say we want to find differentc pieces of what we found
# username is one part and domain is another part
#Like katharguppe33@gmail.com we are interested in
#name=katharguppe and domain=gmail
# the best way to explain this is anything in the first() is in group(1), second search string in group(2)
m = re.search(r'[\w.-]+@[\w.-]+','katharguppe33@gmail.com')
m.group()
m = re.search(r'([\w.-]+)@([\w.-]+)','katharguppe33@gmail.com')
m.group()
m.group(1)
m.group(2)
# If we wanted to find multiple email-ids embedded we could
# another function called find all
# findall finds all occurences of our match
m = re.findall(r'([\w.-]+)@([\w.-]+)','katharguppe33@gmail.com,srinivasks@pes.edu,2015ht1331@bits-pilani.ac.in')
# Here we dont use a group as m returns a list of all finds
# the list would contain tuples if we need to extract part
m = re.findall(r'([\w.-]+)@([\w.-]+)','katharguppe33@gmail.com,srinivasks@pes.edu,2015ht1331@bits-pilani.ac.in')
dir(re)
# dir is a handy option for finding all parameters about python modules
import sklearn as sk # The machine learning package
dir(sk)
# IGNORECASE ignores case, DOTALL includes newline as well so you can process a file as well
m = re.findall(r'([\w.-]+)@([\w.-]+)','katharguppe33@gmail.com,srinivasks@pes.edu,2015ht1331@bits-pilani.ac.in',re.IGNORECASE)
#Let us try an find and print all names as one list and 
# all domains in another list
# Exercise - try this now.
def print_name_domain(str,l1,l2):
    m = re.findall(r'([\w.-]+)@([\w.-]+)','katharguppe33@gmail.com,srinivasks@pes.edu,2015ht1331@bits-pilani.ac.in',re.IGNORECASE)  
    # fill in the missing code so that all names are in l1 and domains in l2 and then iterate thru the list
    #for i in m:
        #if isinstance(i,tuple):
         #   l1.add()
         #   l2.add()
# so the gyan for today is almost done exzcept for pytest which we will cover after these exercise at around 3 pm. 
# for a simple testing functionality
# So lets do one more thing right - write an iterator