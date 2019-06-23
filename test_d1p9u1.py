# -*- coding: utf-8 -*-
"""
Created on Sun May 26 20:52:53 2019

@author: user
"""
# This is the test file
# The test file must always have the pre-fix test
# so save this file as
# test_d1p9u1.py
import d1p9u1 as u1
#import this module for this part
# PIP INSTALL PYTEST
import pytest

# use a special decorator 
#@pytest.mark.skip("reason - this function not used")

# ALL MODULES THAT WE NEED TO TEST MUST HAVE THE PREFIX TEST AND FUNCTIONS
# MUST BE NAMED TEST
def test_calc_total():
    value = u1.calc_total(3,4)
    assert value == 7
def test_calc_multiply():
    value = u1.calc_multiply(7,3)
    assert value == 21
# change to your command prompt and move to the directory
# where at the files are saved
# type python - m pytest
# This will recursively test all your test* files
# You can alternatively use py.test 
# You can use py.test -v
# Exercise 3 : Modify any of your programs for 
# incorrect input and fail these tests
# Push them to a file and extract the files
# such that all failed tests are sorted by name and
# and all failed tests are sorted by name

    
    

