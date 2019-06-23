# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:36:47 2019

@author: user
"""

import cProfile
import d4p14
cProfile.run('d4p14.main()')
# Let us look at all the heading
# percall time tells you the time per function
"""

    ncalls is the number of calls made.
    tottime is a total of the time spent in the given function.
    percall refers to the quotient of tottime divided by ncalls
    cumtime is the cumulative time spent in this and all subfunctions. It’s even accurate for recursive functions!
    The second percall column is the quotient of cumtime divided by primitive calls
    filename:lineno(function) provides the respective data of each function
"""
# This helps understand the time performance of each of these functions
# Run this on the command prompt
# python -m cProfile -o output.txt d4p14.py
import pstats
p = pstats.Stats("output.txt")
p.strip_dirs().sort_stats(-1).print_stats()
# That is much more readable right
# Now run this on recursive functions and see how this works
# say a factorial function
# embed functions and see as to how this works
