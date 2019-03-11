import urllib
import urllib.request
from bs4 import BeautifulSoup

_features = "html.parser"

class _Content():
    def __init__(self,index_url,reg):
        self.in_url = index_url
        self.rul = reg
    
    def By_class(self):
        html = urllib.request.urlopen(self.in_url)
        csoup = BeautifulSoup(html,_features)
        for tmp in csoup.find_all(_class=self.rul)
