# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:54:56 2019

@author: user
"""
# do a easy_install -U memory_profiler
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    my_func()
# python -m memory_profiler d4p16.py
# you can also get into the debug mode
#python -m memory_profiler --pdb-mmem=10 d4p16.py
