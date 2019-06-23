# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:16:08 2019

@author: user
"""

# Tkinter Ikinter little star, how I wonder what you are 
# up about the windows you lie, like a app in the GUI-guy
# applause guys, grades are around the corner
# This is fun and easy to use GUI app development tool kits
# My request is that you convert all of your programs developed in day1,day and day3
# into a nice windowing app. Ya we still use GUI environments
# import tkinter
 # notice the case of the module
 # for those of us familar with design 
 # pattern - tkinter gives us the view  in
 # the MVC pattern
 # when you build a house you need land right
 # to build your house. This land is called
 # the top level window object
 # the top level window object contains all the other parts
 # like your walls, doors, windows, floors
 # but each of them have dependecies
 # like you cant have a door without a wall - atleast sane people dont do that
 # These other objects that you put on top of the land like
 # walls and floors are called widgets

 # of so lets buy land
 # to create a top level window object
 # top = tkinter.Tk()
 # this guy is called the window
 # the top level window shows up stand alone in your application
 # you then design each of your doors and windows i.e widgets
 # widgets can contain widgets like
 # land contains walls , wall have doors and windows and windows can have panes etc
 # you get the drift i.e there is a 
 # hiearchy in the system i.e a parent child relationship
 # each of thes widgets have same properties and behaviors okay methods man
 # such a button pressed, text field filled and they respond to
 # events - such when you press the calling bell
 # you here the door bell - sare jaha se acha
 # the methods the implement this behavior on an event is called a callback
 # example of events are mouse over, exit from text box etc
 # now come the 8-9th floor wizards - architects
 # they would tell us where should we place what and which widget inside which widget etc
 # the the elevations , plans and skecthes they produce
 # all these are done thru geometry managers
 # There are 3 geometry managers
 # Placer - what is the size of each widget and where to place them
 # Packer - packs the widgets within its parent
 # like which glass pane in which position in which window of the real world
 # Grid is used for specifying co-ordinates 
 # we will get to understanding all these shortly
 # but once done we enter the mainloop and wait for events to happen and process them
 # psuedo code
 #  create_top()
 #  create_widgets()
 #  position_them()
 #  enter_mainloop()
 # Subsequently all are handled thru the main loop event processing model
 # There are 18 odd widgets like button, label, menu, entry
 # Self Note: draw this on the board
 # Our best friend is the default
 # So let us do hello world
 # import tkinter
 # top= tkinter.Tk()
 #label=tkinter.Label(top,text="Hello SPoners")
 #label.pack()
 # labels are what they are labels
 # let us add buttons
 # Let us dissect each of these now thru simple programs