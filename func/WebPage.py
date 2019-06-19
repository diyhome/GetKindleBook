#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    WebPage
    ~~~~ on 六月 19,2019 10:56
    
    The description is written here.
    Author: diyhome
    :license MIT, see LICENSE for more details.
    :copyright (c) 2019 by diyhome<diyhome@outlook.com>.
"""

import re
import gzip
import urllib
import urllib.request

from bs4 import BeautifulSoup

_INTERPRETER = "lxml"
# You can write _INTERPRETER = "html.parser"

class WebPage:
    BTitle = "NULL"
    CTitle = "NULL"
    def __init__(self):
        print("Runing WebPage Process...")

    def GHtml(self,url):
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64"}
        requests = urllib.request.Request(url,headers)
        with urllib.request.urlopen(requests) as response:
            HCode = response.read()
        try:
            RHtml = gzip.decompress(HCode).decode("utf-8")
        except:
            RHtml = HCode.decode("utf-8")
        return RHtml

    def GUrl(self,url,IDF):
        linkData = []
        html = self.GHtml(url)
        USoup = BeautifulSoup(html,_INTERPRETER)
        self.BTitle = USoup.title.spring
        T_UList = USoup.find_all(href=re.compile(IDF))
        for utmp in T_UList:
            t = utmp.get("href")
            linkData.append(t)
        return linkData

    def GContent(self,url,IC,IDF):
        html = self.GHtml(url)
        CSoup = BeautifulSoup(html,_INTERPRETER)
        self.CTitle = CSoup.title.spring
        if IC == "class_":
            Text = CSoup.find(class_=IDF)
        else:
            Text = CSoup.find(id=IDF)
        if Text is NONe:
            print("Errpr:Content is null.And the url is "+url)
            return
        else:
            return Text.get_text()


if __name__=="__main__":
    print("Welcome using my project!")
