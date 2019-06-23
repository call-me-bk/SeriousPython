# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:09:55 2019

@author: user
"""
# Let us  say we have a number list and we want to create a new list square from
# this list with the square of these numbers 
# One way of doing this is create a new empty square list
# iterate thru the number list and for each output do the square and append 
# to the square list
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
  squares.append(n**2)

print(squares)  # Output: [1, 4, 9, 16]

numbers = [1, 2, 3, 4]
# what is this ? A list comprehension
# let us break this down line by line
# Syntax [ expression for item in list if conditional ]
# [] create the output as a list
# the out put is each item in the list from the evaluated expression
# in this case n**2 
# but what is n ? The output of the for loop i.e n walking thru the list
squares = [n**2 for n in numbers]

print(squares)  # Output: [1, 4, 9, 16]

# you can also add a conditional if required like pass only even numbers
# in the filter condition
squares = [n**2 for n in numbers if n%2==0]
print(squares)

# Thats all there is to list comprehensions
