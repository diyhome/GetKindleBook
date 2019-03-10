import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
indexurl = "http://www.156zw.net/html/0/596/index.html"

def geturl(index_url):
    html = urllib.request.urlopen(index_url)
    surl = BeautifulSoup(html,'html.perar')
    print(surl.prettify())

if __name__ == "__main__":
    geturl(indexurl)
