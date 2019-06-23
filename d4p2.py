#!/usr/bin/env python

import tkinter
# Create a top level window i.e land
top = tkinter.Tk()
# Now get the name board done for your land i.e top and call it hello world
label = tkinter.Label(top, text='Hello World!')
# Now pack the name board on the land
label.pack()
label.config(text='My Life My Rules')
# now wait for the contractor to arrive which is for ever
tkinter.mainloop()

# in the pack options try the following
#expand=True
#fill=None |X|Y|Both i.e each of these are mutually exclusive
