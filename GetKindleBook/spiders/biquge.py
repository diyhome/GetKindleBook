# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from GetKindleBook.items import EbookItem


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['https://www.biquge.com.cn']
    start_urls = ['https://www.biquge.com.cn/book/19074/']

    def parse(self, response):
        item = EbookItem()
        selsector = Selector(response)
        find_all = selsector.xpath('//*[@id="list"]/dl/dd')
        # print(find_all)
        BookName = selsector.xpath('//*[@id="info"]/h1/text()').extract_first()
        Anouthor = selsector.xpath('//*[@id="info"]/p[1]/text()').extract()
        # print(Anouthor)
        item['BookName'] = BookName
        item['Anouthor'] = Anouthor
        for section in find_all:
            href = section.xpath('.//@href').extract_first()
            UrlChate = response.urljoin(href)
            request = scrapy.Request(UrlChate,callback=self.parse_detail)
            yield request

    def parse_detail(self,response):
        selector = Selector(response)
        content_list = selector.xpath('//*[@id="content"]')

