from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

site = "http://en.wikipedia.org/wiki/StackOverflow"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site, headers=hdr)
r = urlopen(site).read()

soup = BeautifulSoup(r)
print (type(soup))