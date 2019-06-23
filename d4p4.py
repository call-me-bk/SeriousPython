#!/usr/bin/env python

import tkinter
top = tkinter.Tk()

hello = tkinter.Label(top, text='Hello World!')
hello.pack()

quit = tkinter.Button(top, text='QUIT',
    command=top.quit, bg='red', fg='white')
#fg = foreground, bg=background
quit.pack(fill=tkinter.X, expand=1)
#quit.pack(fill=tkinter.Y, expand=1)
#fill=X means make this widget as wide as parent
#expand=True means fill any space that has not been used in
#the parent widget


tkinter.mainloop()
# Let us change fill=Y and see what happens