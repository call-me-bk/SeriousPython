# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:40:17 2019

@author: user
"""

# so what are threads - these are independently running instructions in a single
# process space - need not be the same processor
# Let me explain this with a drawing for you
# Most of us have octa core phone - which means each core(~= processor)
# can each run a process
# All of play PUBG, NFS, GTA each player can be running independently i.e as threads
# if I see my process explorer I am darn sure I would see 2000+ threads running
class Hello:
    def run(self):
        for i in range(5):
            print("hello")
class Hi:
    def run(self):
        for i in range(5):
            print("hi")
t1 = Hello()
t2 = Hi()
t1.run()
t2.run()
# These guys run one after the other right?
# How can we make them run parallely and then make
# them meet at some adda
# The default is always one Main Thread
from threading import *
from time import sleep
class TrHello(Thread):
    def run(self):
        for i in range(5):
            print("Thello")
            sleep(1)
class TrHi(Thread):
    def run(self):
        for i in range(5):
            print("Thi")
            sleep(1)
# I have intentionally used run whichh is a method
# Now let us run
t3 = TrHello()
t4 = TrHi()
t3.run()
t4.run()
# Nope same result
# for it to run concurrently we need start
t3.start()
sleep(0.2)
t4.start()
# But bye got printed because it was in the main thread
# so use join()
t3.join()
t4.join()
print("Bye")
# Now let us define some functions and run them as threads
# Python program to illustrate the concept 
# of threading 
# importing the threading module and pass parameters
import threading 

def print_cube(num): 
	""" 
	function to print cube of given num 
	"""
	print("Cube: {}".format(num * num * num)) 

def print_square(num): 
	""" 
	function to print square of given num 
	"""
	print("Square: {}".format(num * num)) 

if __name__ == "__main__": 
	# creating thread 
	t1 = threading.Thread(target=print_square, args=(10,)) 
	t2 = threading.Thread(target=print_cube, args=(10,)) 

	# starting thread 1 
	t1.start() 
	# starting thread 2 
	t2.start() 

	# wait until thread 1 is completely executed 
	t1.join() 
	# wait until thread 2 is completely executed 
	t2.join() 

	# both threads completely executed 
	print("Done!") 



