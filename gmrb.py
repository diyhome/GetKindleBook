from func.chater import Chater
from func.content import Content

gmrb = Content()
links = gmrb.GUrl("http://guancha.gmw.cn/",'/content_')
con = gmrb.GText(links[-5],"class_","u-mainText")
print(con)

