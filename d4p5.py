#!/usr/bin/env python

from tkinter import *

# Nothing new in this module other than that we
# have a scale widget
# and we implement the resize as a command

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % \
        scale.get())

top = Tk()
# Specified in pixels
top.geometry('250x150')

label = Label(top, text='Hello World!',
    font='Helvetica -12 bold')
# Fill this vertically and  expand whatever space is left for by the main window
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=10, to=40,
    orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

quit = Button(top, text='QUIT',
    command=top.quit, activeforeground='white',
    activebackground='red')
# Focus is set to the quit button
quit.focus_force()
quit.pack()

mainloop()
