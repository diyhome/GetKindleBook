# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from GetKindleBook.items import EbookItem


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['biquge.com.cn']
    start_urls = ['https://www.biquge.com.cn/book/39269/']
    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        # "CONCURRENT_REQUESTS_PER_DOMAIN": 2
    }


    def parse(self, response):
        selsector = Selector(response)
        print(response)
        find_all = selsector.xpath('//*[@id="list"]/dl/dd')
        num = 0
        for section in find_all:
            num += 1
            href = section.xpath('.//@href').extract_first()
            UrlChate = response.urljoin(href)
            request = scrapy.Request(UrlChate, callback=self.parse_detail, meta={'num': num})
            yield request

    def parse_detail(self, response):
        xzbq = Selector(response)
        huan= xzbq.xpath('//*[@id="content"]/text()').extract()
        conn = xzbq.css('#wrapper > div.content_read > div > div.bookname > h1::text').extract_first()
        # cont = "\n".join(huan) #{'a','b','c'} -> a-b-c
        item = EbookItem()
        item['num'] = response.meta['num']
        item['ChaterNa'] = conn
        item['ChaterCo'] = huan
        yield item