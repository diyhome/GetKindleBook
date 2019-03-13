#!/usr/bin/python3
import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
import re

urls='http://guancha.gmw.cn/'
save_path = os.getcwd()+"/save/"

def get_urls():
    linkData = []
    html = urllib.request.urlopen(urls)
    soup_url = BeautifulSoup(html,'lxml')
#    print(soup_url.prettify()
    list_url = soup_url.find_all(href=re.compile("/content_"))
    for utls in list_url:
        datas = utls.get('href')
        if datas.startswith('http'):
            linkData.append(datas)
            #  print("http:"+datas)
        elif datas.startswith('https'):
            linkData.append(datas)
        else:
            linkData.append(urls+datas)
            #  print(urls+datas)
    #  print(datas)
    #  print(linkData)
    return(linkData)

def get_content(link_):
    print(link_)
    dat = re.search(r"(\d{4}-\d{1,2}/\d{1,2})",link_)
    #  print(dat.group(0))
    html = urllib.request.urlopen(link_).read().decode('utf-8')
    soup = BeautifulSoup(html,'lxml')
    titmp = soup.title.string
    tit=""
    for i in titmp:
        if is_chinese(i):
            tit = tit+i
    contmp = soup.find(class_='u-mainText')
    #  print (contmp)
    if contmp:
        #  print(contmp)
        contmp = contmp.get_text()
    else:
        #  print(link_)
        return
    conlist = contmp.split()
    contents = ""
    for index in range(len(conlist)-7):
        contents = contents+conlist[index]+"    \n"
    save_(tit,contents,dat)
    #  send_kindle(tit,contents,dat)

def save_(tit,contents,dat):
    f = open(save_path+tit+".md","w+")
    #  print("succ")
    f.write("#"+tit+"\n"+
            contents)
    f.close()

def send_kindle(tit,contents,dat):
    f = open(save_path+"光明时评.txt","a+")
    f.write("#"+tit+"\n"+contents+"\n 日期: "+dat.group(0)+"\n"+"\n")
    f.close()

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

if __name__ == '__main__':
    _link = get_urls()
    #  get_content(_link[3])
    for url_ in _link:
        get_content(url_)
