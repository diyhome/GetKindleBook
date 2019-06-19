#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    gmrb
    ~~~~ on 六月 19,2019 13:20
    
    The description is written here.
    Author: diyhome
    :license MIT, see LICENSE for more details.
    :copyright (c) 2019 by diyhome<diyhome@outlook.com>.
"""

from func.WebPage import WebPage

if __name__=="__main__":
    gmrb=WebPage()
    links = gmrb.GUrl("http://guancha.gmw.cn/",'/content_')
    print(links)
    print(gmrb.GContent("http://guancha.gmw.cn/2019-04/11/content_32760212.htm","class_","u-mainText"))