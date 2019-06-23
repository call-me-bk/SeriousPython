#!/usr/bin/env python

import tkinter as tk

top = tk.Tk()
# Here we are a creating a widget of class button
# with a command saying quit i.e invoking the call back function
# of top
dir(top)
def lbl_change(ev=None):
   pass
quit = tk.Button(top, text='quit',
    command=top.quit)
quit.pack(side = tk.LEFT)
# so far we have learnt the following
# config of set variables
# command for execution of certain variables
# let us create one more button called ok
ok = tk.Button(top, text='ok',
    command=lbl_change)
ok.pack(side = tk.RIGHT)
label = tk.Label(top, text='Hello World!')
label.pack()
tk.mainloop()
