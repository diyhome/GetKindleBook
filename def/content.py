import re
import urllib
import urllib.request
from bs4 import BeautifulSoup

_features = "html.parser"

class Content:
    tit="null"
    def __init__(self):
        print("Runing Content class...")
        """防止重复调用是tit保留上一次内容"""
        tit = "null"
    
    def GUrl(self,url,sre):
        linkData = []
        html = urllib.request.urlopen(url)
        csoup = BeautifulSoup(html,_features)
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
    def GText(self,url,ic,sre):
        html = urllib.request.urlopen(url)
        tsoup = BeautifulSoup(html,_features)
        Text = tsoup.find(ic=sre)
        if Text == "":
               print("Content is null.Faild:"+url)
               return
        else:
            #  Text = Text.get_text()
            return Text

if __name__ == "__main__":
    ur = Content()
    #  ul=ur.GUrl('http://guancha.gmw.cn/','/content_')
    #  print(ul)
    tc=ur.GText('http://news.gmw.cn/2019-03/01/content_32584315.htm',"class_","u-mainText")
    print(tc)
