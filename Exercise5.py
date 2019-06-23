import requests, os, bs4
from threading import *
from time import sleep

#i had issues with this submission, so Afzal Mukhtar helped me out, but sir i want you to demonstrate this code to me

url = 'http://xkcd.com' # starting url
os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd
# Download the page.

global comicUrl, done
comicUrl, done = set(), set()


def URL(url):
    i = 0
    while not url.endswith('#') and i < 2500 and done.intersection({url}) == set():
        print('Reading page %s...' % url)
        done.add(url)
        try:
            res = requests.get(url, timeout = 3)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text)
        except: 
            print("Connection TimeOut")
            continue
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []: print("Invalid Link")
        elif comicElem[0].get('src').startswith("//"):
            comicUrl.add(str('http:'+comicElem[0].get('src')))
                #Add the url to the list
        else: print("Broken Link...")
        # Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
        i += 1


def Download(comicUrl):
    # Download the image.
    for i in comicUrl:
        path_name = "E:/College Courses/Summer Courses/Serious Python/Day2/Exercise/xkcd/"+os.path.basename(i)
        if not os.path.exists(path_name) and done.intersection({i}) == set():
            done.add(i)
            try:
                print('Downloading image %s...' % (i))
                res = requests.get(i, timeout = 3)
                res.raise_for_status()
            except: 
                print("Broken Link...") 
                continue
            # Save the image to ./xkcd
            
            imageFile = open(os.path.join('xkcd', os.path.basename(i)), 'wb')
            for chunk in res.iter_content(10000):
                imageFile.write(chunk)
            imageFile.close()

threads = []
url_threads = []

for i in range(8):
    u = Thread(target = URL, args = (url,))
    url_threads.append(u)
    u.start()

for u in url_threads:
    u.join()


for i in range(8):
     t = Thread(target = Download, args = (list(comicUrl), ))
     threads.append(t)
     t.start()
     sleep(0.2)

for t in threads:
    t.join()

print("Done..")