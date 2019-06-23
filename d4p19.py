# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 20:24:20 2019

@author: user
"""

import re
match=re.match(r'abc','abcd')
type(match)
import inspect
inspect.getmembers(match)
inspect.isclass(match)
inspect.iscode(match)
def x():
    for i in range(10):
        print(i)
inspect.isfunction(x)
inspect.getsourcelines(x)
class x :
    pass 
class y(x):
    pass
class z(y):
    pass
inspect.getclasstree([x,y,z])      
#not so readable but useful when used with pprint
