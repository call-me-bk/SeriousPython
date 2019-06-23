# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:49:14 2019

@author: user
"""
# The last topic for the day
# Combining test cases example  using 
#typically bva says that check near the edge condition
import d1p9u1 as u1
import pytest
def test_calc_total_1():
    x = u1.calc_total(3,4)
    assert x == 7
def test_calc_total_2():
    x = u1.calc_total(4,4)
    assert x == 8
def test_calc_total_3():
    x = u1.calc_total(4,3)
    assert x == 7
# How could I avoid code duplication
# how nice if we could pass input and output as 
# parameters
@pytest.mark.parametrize("i1,i2,o",
                         [
                                 (5,4,9),
                                 (4,5,9),
                                 (4,-4,0)
                        ]
                        )
def test_calc_total(i1,i2,o):
    value = u1.calc_total(i1,i2)
    assert value == o
# and then go back and add a decorator for parameters
