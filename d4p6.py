#!/usr/bin/env python

from functools import partial as pto
# this partial function application is just stacked functionality
from tkinter import Tk, Button, X
from tkinter.messagebox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU,
}
# see I told you that we would use lambda
# Recollect that lamdba as oneline function of
# lamba capture parameter: code black execution
critCB = lambda : showerror('Error', 'Error Button Pressed!')
warnCB = lambda : showwarning('Warning',
    'Warning Button Pressed!')
infoCB = lambda : showinfo('Info', 'Info Button Pressed!')
# showerror... etc are al dialog boxes
top = Tk()
top.title('Road Signs')
Button(top, text='QUIT', command=top.quit,
    bg='red', fg='white').pack()
# see the function tools and import partial , everything else is simple in this code
MyButton = pto(Button, top)
#Here I am stating the there is a function called which always has the top parameter
# There is the second level of indirection here
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
ReguButton = pto(MyButton, command=infoCB, bg='white')

# critical function has attributes of mybutton which has attributes of button which has attributes of top
# thats all just like class inheritance with parameters defaulted at each level
for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (
        signType.title(), eachSign,
        '.upper()' if signType == CRIT else '.title()')
    print(cmd)
    # executes expresssion passed as a parameter after evaluation
    eval(cmd)
    # In this case instant of button created

top.mainloop()
