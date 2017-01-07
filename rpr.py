from urllib.request import urlopen
from bs4 import BeautifulSoup


web_page = urlopen("http://reddit.com")
soup = BeautifulSoup(web_page, 'html.parser')

mydivs = soup.findAll("a", { "class" : "title" })
for div in mydivs:
    print(div.text)
