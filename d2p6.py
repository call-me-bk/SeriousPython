#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
# Ok lets look at another protocol http


import webbrowser, sys

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    webbrowser.open('https://www.google.com/maps/place/' + address)
else:
    # Get address from clipboard.
    address = 'Bangalore'
    webbrowser.open('https://www.google.com/maps/place/' + address)

# a few things here sys.argv[] is contains all command line parameters
# http - stands for hypertext transfer protocol
# there are 3 important things to remember
# connectionless 
# media independent
# stateless
# http primary mechanisms are 
# 1 send a request() close()
# 2.send a response() close()
# watch this video for a quick understanding of request and response
# https://youtu.be/eesqK59rhGA
# Think of http as a messenger
# you can send text,  video, audio etc
# http is an application level protocol and which means
# the 2 systems that need to communicate must be physically connected
# and able to connect with each other http uses TCP communication
# http is defined by rules - so has rigor in it
# http is all text (not actually)divided into 3 parts
# Request 
# -------
# start , header and body
# body can contain binary data 
# start line contains some methods asking what to do
# GET, POST etc and then what to get or post and the version of http
# headers contains name, value pairs like what language, data content  etc
# Response
# --------
# start line contains
# version of http
# contains status code
# 200 ok
# 404 file not found
# header contains name value pairs
# and finally the body contains the actual file itself
# This groslly simplified
# but enough for our purpose for http
#-------------------------------------
# to get going we need to import
import requests
#let us send a request
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# let us examine this guy
type(res)
# what are its properties
dir(res)
# what is the url,status_code
print(res.url+str(res.status_code))
# what text came in the body
print(res.text)
print(len(res.text))
# so what is the file is not found - how do we gracefully handle this
res = requests.get('https://automatetheboringstuff.com/files/page_that_does_not_exist')
#there is a method for handling this stuff
# raise_for_status()
import requests
res = requests.get('https://automatetheboringstuff.com/files/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('%s' %(exc))
# for a file found
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('%s' %(exc))
#we have a nice method call iter_content which returns the text in chunks of 
#the parameter specified
import requests
import os
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
    playFile=open('RomeoAndJuliet.txt','wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
except Exception as exc:
    print('%s' %(exc))
# now that you now how to download files and videos etc
# Yesterday I wanted you to use regular expressions to parse HTML
# but like every Prof today I dont want you to do it
# There is this very nice module called beautiful soup which can help you 
# parse HTML
# So let us import this guy
import requests, bs4
# There is a nice function called beautufulsoup that returns
# what else soup not ketchup object with which we can do a variety of things
# so lets have some fun
res=requests.get('https://www.pes.edu') 
# lets get the soup out of the way
soup=bs4.BeautifulSoup(res.text)
print(soup)
print(type(soup))
#me no teach html but we all know html, div,#author which are all elements of HTML
print(soup.select('#author'))
# :(  no author
print(soup.select('div'))
# Let us use a URL which has these elements filled in
res=requests.get('https://nostarch.com') 
# lets get the soup out of the way
soup=bs4.BeautifulSoup(res.text)
element=(soup.select('div'))
for i in range(100):
    print(element[i])
# There are other nice elements of beutuful soup
# Let us explore some of them
# soup.find_all('b') - Finds all the b tags
# print soup.find_all(["a", "b"]) find all tags a  and b
# for tag in soup.find_all(True):
#    print(tag.name)
# prints all tags
# Read about this in https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python
# for doing the exercise - The topic here is http and so 
# I have not gone into details