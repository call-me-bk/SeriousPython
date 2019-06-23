# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:31:08 2019

@author: user
"""

"""
Memoization is an optimization technique used to speed up 
function calls by caching their results."""
import functools
import math
@functools.lru_cache(maxsize=2)
def memoized_sin(x):
     return math.sin(x)
memoized_sin(2)
memoized_sin.cache_info()
memoized_sin(2)
memoized_sin.cache_info()
memoized_sin(3)
memoized_sin.cache_info()
# This is wonderful way of speeding up your code
# a often used technique in my oracle day but in c++
# for those of you who have done dbms
# this is keep for sp and pin for table
# storing tables in memory
