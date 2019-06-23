# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:47:18 2019

@author: user
"""
import py9
def test_calc_total():
    result = py9.calc_total(3,4)
    assert result == 7
def test_calc_multiple():
    result = py9.calc_multiply(3,4)
    assert result == 12
    