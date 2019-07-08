#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    setup
    ~~~~ on 六月 20,2019 18:40
    
    The description is written here.
    Author: diyhome
    :license MIT, see LICENSE for more details.
    :copyright (c) 2019 by diyhome<diyhome@outlook.com>.
"""
import sys

from scrapy.cmdline import execute


# execute(['scrapy', 'crawl', 'xiaoshuobi','-a','links=https://www.xiaoshuobi.cc/read/87472/'])

def start(link):
    tlink = "links=" + link
    sname = link.split(".")[1]
    execute(['scrapy', 'crawl', sname, '-a', tlink])


if __name__ == "__main__":
    urls = sys.argv[1:]
    for url in urls:
        start(url)
