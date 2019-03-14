#!/usr/bin/env python3
from func.chater import Chater
from func.content import Content
from func.FSave import FSave as f

gmrb = Content()
cs = Chater()
links = gmrb.GUrl("http://guancha.gmw.cn/",'/content_')
#  con = gmrb.GText(links[-5],"class_","u-mainText")
#  tit = gmrb.tit
#  tmp = tit.split('_',1)
#  print(tmp[:1])
for i in links:
    con = gmrb.GText(i,"class_",'u-mainText')
    #  print(con)
    t = cs.onchinese(gmrb.tit)
    f('/save/gmrb/',t,con,'w+')
