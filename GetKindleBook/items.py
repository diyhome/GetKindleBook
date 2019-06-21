# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EbookItem(scrapy.Item):
    num = scrapy.Field()
    ChaterNa = scrapy.Field()
    ChaterCo = scrapy.Field()

class BookDetail(scrapy.Item):
    bname = scrapy.Field()
    muser = scrapy.Field()
