# -*- coding: utf-8 -*-
"""
Created on Sun May 26 20:52:53 2019

@author: user
"""

import d1p9u1 as u1
import pytest
import sys
# I only want to test functions that kave multiply as name
# use py.test -k with_the_name
def test_calc_total():
    value = u1.calc_total(3,4)
    assert value == 7

def test_calc_multiply():
    value = u1.calc_multiply(7,3)
    assert value == 21
# You would only see tests that running for multiply
# you can use decorators and -k options as well
#-----------------------------
# Let us use custom markers



    
    

