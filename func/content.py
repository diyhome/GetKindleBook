#!/usr/bin/env python3
import re
import urllib
import urllib.request

from bs4 import BeautifulSoup

#  _features = "lxml"
_features = "html.parser"

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
        Text = ""
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
    print("你可以通过编辑main函数测试!")
