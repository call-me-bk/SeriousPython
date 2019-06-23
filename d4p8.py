# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:13:58 2019

@author: user
"""

from tkinter import *
#import tkMessageBox
import tkinter
from tkinter.messagebox import showinfo, showwarning, showerror
def myrand(ev=None):
  showinfo('Info', 'Something Pressed')

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()
Lb1.bind('<<ListboxSelect>>', myrand)
top.mainloop()
#if you have an insert you will have a delete
# thats quite easy.
# Now that you have all the tools required 
# quickly walk thru p4d9
# observe the event listner parameters in bind