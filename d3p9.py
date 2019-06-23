# -*- coding: utf-8 -*-
"""
Created on Thu May 30 08:33:37 2019

@author: user
"""

import openpyxl
wb=openpyxl.load_workbook('example.xlsx')
dir(wb)
# try to figure out what type of an object is wb
# try and see what are the sheets available in the wb
x=wb.get_sheet_names() # deprecated
print(x)

# we see that x is a list of sheets
# to access a particluar sheet
sheet = wb.get_sheet_by_name('Sheet1')
sheet.title = 'Sheet1'
print(sheet.title)
c=sheet['A1'].value
print(c)
wb.create_sheet(index=0, title='1st Sheet')
wb.save('example.xlsx')
# fairly simple stuff
# How about some more serious stuff


