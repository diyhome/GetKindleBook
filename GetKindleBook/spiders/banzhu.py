# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from GetKindleBook.items import EbookItem, BookDetail


class BanzhuSpider(scrapy.Spider):
    name = 'banzhuer'
    allowed_domains = ['banzhuer.com']
    custom_settings = {
        "DOWNLOAD_DELAY": 0.01,
    }
    def __init__(self, links=None, *args, **kwargs):
        super(BanzhuSpider, self).__init__(*args, **kwargs)
        self.start_urls = [links]

    def parse(self, response):
        selsector = Selector(response)
        xz = BookDetail()
        print(response)
        find_all = selsector.xpath('//*[@id="list"]/dl/dd[position()>9]/a')   #这网站有毒,前九章是最新更新的,避免选择前九章
        xz['bname'] = selsector.xpath('//*[@id="info"]/h1/text()').extract_first()
        xz['muser'] = selsector.xpath('//*[@id="info"]/p[1]/text()').extract_first().replace("\xa0", '')
        yield xz
        num = 0
        for section in find_all:
            num += 1
            href = section.xpath('.//@href').extract_first()
            UrlChate = response.urljoin(href)
            request = scrapy.Request(UrlChate, callback=self.parse_detail, meta={'num': num})
            yield request

    def parse_detail(self, response):
        xzbq = Selector(response)
        huan = xzbq.xpath('//*[@id="content"]/text()').extract()
        conn = xzbq.css('div.content_read > div > div.bookname > h1::text').extract_first()
        item = EbookItem()
        item['num'] = response.meta['num']
        item['ChaterNa'] = conn
        item['ChaterCo'] = huan
        yield item
