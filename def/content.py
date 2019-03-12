import re
import urllib
import urllib.request
from bs4 import BeautifulSoup

_features = "lxml"

class Content:
    tit="null"
    def __init__(self):
        print("Runing Content class...")
        """防止重复调用是tit保留上一次内容"""
        tit = "null"
        self.page = "Loading..."
        self.content = "Loading..."
    
    def GUrl(self,url,sre):
        linkData = []
        html = urllib.request.urlopen(url)
        csoup = BeautifulSoup(html,_features)
        self.page = csoup.prettify()
        #  print(csoup.prettify())
        url_list = csoup.find_all(href=re.compile(sre))
        #  print(url_list)
        for tmp in url_list:
            t = tmp.get('href')
            #  print(t)
            if t.startswith('http://'):
                linkData.append(t)
            else:
                linkData.append(url+t)
        return linkData
    def GText(self,urls,ic,sre):
        html = urllib.request.urlopen(urls)
        tsoup = BeautifulSoup(html,_features)
        self.content = tsoup.prettify()
        #  Text = tsoup.find(class_=sre)
        if ic == "class_":
            Text = tsoup.find(class_=sre)
            #  print("Runing GText class")
        else:
            Text = tsoup.find(id=sre)
        if Text is None:
               print("Content is null.Faild:"+url)
               return
        else:
            #  Text = Text.get_text()
            return Text.get_text()
    def ts(self,url):
        html = urllib.request.urlopen(url)
        s = BeautifulSoup(html,_features)
        print(s.prettify())

if __name__ == "__main__":
    url = input("Enter url:")
    print("Your Entent: +\n"
            +url+"\n"
            +rs+"\n"
            +rss+"\n")
    r = Content()
    #  url = "http://guancha.gmw.cn/"
    #  rs = "/content_"
    #  iurl = r.GUrl(url,rs)
    #  print(iurl)
    #  print(r.content)
    #  s = r.GText(iurl[-5],"class_","u-mainText")
    #  print(s)
    print(r.ts(url))
    urls = r.GUrl(url,rs)
    print(urls)
    cu = urls[-5]
    print(r.ts(cu))
    rss = input("Re content:")
