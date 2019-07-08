# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.selector import Selector

from GetKindleBook.items import EbookItem, BookDetail


class XiaoshuobiSpider(scrapy.Spider):
    name = 'xiaoshuobi'
    allowed_domains = ['xiaoshuobi.cc']
    trueurl = 'https://www.xiaoshuobi.cc/files/article/html555/'
    custom_settings = {
        "DOWNLOAD_DELAY": 0.01,
    }

    def __init__(self, links=None, *args, **kwargs):
        super(XiaoshuobiSpider, self).__init__(*args, **kwargs)
        self.start_urls = [links]

    def parse(self, response):
        selsector = Selector(response)
        Intruction = BookDetail()
        find_all = selsector.xpath('//*[@id="list"]/dl/dd[position()>9]/a')
        Intruction['bname'] = selsector.xpath('//*[@id="info"]/h1/text()').extract_first()
        Intruction['muser'] = selsector.xpath('//*[@id="info"]/p[1]/text()').extract_first().replace("\xa0", '')
        yield Intruction
        num = 0
        for section in find_all:
            num += 1
            href = section.xpath('.//@href').extract_first()
            ChapterName = section.xpath('.//text()').extract_first()
            ID_List = re.findall('\d+', href)
            BookID = ID_List[1]
            ChapterID = ID_List[2]
            UrlChapter = self.trueurl + BookID[0:2] + '/' + BookID + '/' + ChapterID + '.html'
            request = scrapy.Request(UrlChapter, callback=self.parse_detail, meta={'num': num, 'CN': ChapterName})
            yield request

    def parse_detail(self, response):
        BookContent = Selector(response)
        TBookText = BookContent.xpath('.//text()').extract()
        BookText = self.ReKey(TBookText)
        item = EbookItem()
        item['num'] = response.meta['num']
        item['ChaterNa'] = response.meta['CN']
        item['ChaterCo'] = BookText
        yield item

    def ReKey(self, Content=[]):
        ReKey_List = re.findall(r".replace(.*)", Content[-1])
        var = "$%##^^^%$".join(Content)
        for EachOne in ReKey_List:
            key = EachOne.split(",")
            BKey = self.IsChinese(key[0])
            AKey = self.IsChinese(key[1])
            var = var.replace(BKey, AKey)
        return var.split("$%##^^^%$")

    def IsChinese(self, str):
        pattern = re.compile("[\u4e00-\u9fa5]")
        if str == "\'，\');":
            return "，"
        return "".join(pattern.findall(str))
