# -*- coding: utf-8 -*-
"""
Created on Sun May 26 20:52:57 2019

@author: user
"""

# I only test my code in production
# There are various tests done at various points
# unit test, integration, acceptance tests
# an Important characteristic is that tests should
# be regressible i.e as we fix code we need to test

# Serious code involves FURPS+ coverage
# Lets get functional testing automated today

# There are various testing frameworks but lets us test
# using pytest, others are nose and unittest

# Q? what does this evaluate to
#while (1==2):
#    pass
# my version of math lib
def calc_total(a,b):
    return a+b
def calc_multiply(a,b):
    return a*b