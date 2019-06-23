# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:47:18 2019

@author: user
"""
# in your conda prompt
#install pytest pip install pytest
# prefix filenames with test (mandatory)
# all test functions MUST have a test_ ( mandatory)
import py9
import pytest
import sys
#@pytest.mark.skip(reason = "I dont run this now")
def test_calc_total():
    result = py9.calc_total(3,4)
    assert result == 7
def test_calc_multiple():
    result = py9.calc_multiply(3,4)
    assert result == 12
    
#@pytest.mark.skipif(sys.version_info > (3,5), reason ="Not compatible")
def test_mult():
    result = py9.calc_multiply(3,4)
    assert result == 12
    # conda prompt py.test filename{teststub}
# selective ignore test by the ignore options    
# --ignore test_py91.py ignore 
# --ignore-global allows wild cards
# lets copy test_py9.py to test_py91.py
#pytest -v -rxs for the reason for skipping
#pytest -k for including only certain function names
#pytest -m for only those mark
@pytest.mark.WINDOWS
def test_mytest():
    assert True
@pytest.mark.UNIX
def test_my_unix_test():
    assert True
# run pytest -v -rxs -k mult
# run pytest -m WINDOWS
# run pytest - m "not WINDOWS"
