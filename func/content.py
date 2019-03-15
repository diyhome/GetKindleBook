#!/usr/bin/env python3
import re
import urllib

from urllib import request
from urllib import error
from bs4 import BeautifulSoup

_features = "lxml"
#  _features = "html.parser"

class Content:
    tit="null"
    def __init__(self):
        print("Runing Content class...")

    def GUrl(self,url,sre):
        linkData = []
        html = self.htmlcode(url)
        csoup = BeautifulSoup(html,_features)
        url_list = csoup.find_all(href=re.compile(sre))
        for tmp in url_list:
            t = tmp.get('href')
            if t.startswith('http://'):
                linkData.append(t)
            else:
                linkData.append(url+t)
        return linkData
    def GText(self,url,ic,sre):
        tit = None
        html = self.htmlcode(url)
        tsoup = BeautifulSoup(html,_features)
        self.tit = tsoup.title.string
        self.content = tsoup.prettify()
        if ic == "class_":
            Text = tsoup.find(class_=sre)
        else:
            Text = tsoup.find(id=sre)
        if Text is None:
            print("Content is null.Faild:"+url)
            return
        else:
            return Text.get_text()
    def htmlcode(self,url):
        headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
        req = request.Request(url=url,headers=headers)
        try:
            response = request.urlopen(req)
            html = response.read()
            return html
        except error.URLError as e:
            print(e.reason)

if __name__ == "__main__":
    print("你可以通过编辑main函数测试!")
