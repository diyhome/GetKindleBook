#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    BiQuGe
    ~~~~ on 六月 19,2019 20:58
    
    The description is written here.
    Author: diyhome
    :license MIT, see LICENSE for more details.
    :copyright (c) 2019 by diyhome<diyhome@outlook.com>.
"""

MUrl = "https://www.qu.la/book/1983/"
IDF = "/book/1983"
from func.FSave import FSave as sa
from func.WebPage import WebPage

if __name__ == "__main__":
    bqg = WebPage()
    links = bqg.GUrl(MUrl, IDF)
    Bt = bqg.BTitle
    for l in links:
        Contents = bqg.GContent(MUrl + l, "id", "content")
        CBt = bqg.CTitle
        print(CBt)
        sa("save", Bt + ".txt", CBt + "\r\n" + Contents + "\r\n", "a")
