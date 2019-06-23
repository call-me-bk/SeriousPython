# -*- coding: utf-8 -*-
"""
Created on Mon May 27 08:09:12 2019

@author: user
"""

# Running and skipping tests selectively
import d1p9u1 as u1
import pytest
#-----------------------------
# Let us use custom markers
# @pytest.mark.windows
# you can name this marker anything windows, srini, ram

# you can see that I have marked some as windows and some as mac
# with py.test -m mac only mac test run and -m windows only...
@pytest.mark.windows
def test_windows_1():
    assert True
@pytest.mark.windows
def test_windows_2():
    assert True
@pytest.mark.mac
def test_mac_1():
    assert True
@pytest.mark.mac
def test_mac_2():
    assert True
#-----------------------------
# Let us use custom markers
