# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Anouthor = scrapy.Field()
    BookName = scrapy.Field()
    ChaterNa = scrapy.Field()
    ChaterCo = scrapy.Field()
    UrlChate = scrapy.Field()
