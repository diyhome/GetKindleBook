# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from GetKindleBook.items import BookDetail
from GetKindleBook.items import EbookItem


class RzxswSpider(scrapy.Spider):
    name = 'RZXSW'
    allowed_domains = ['www.rzlib.net']
    start_urls = ['https://www.rzlib.net/b/85/85651/']
    custom_settings = {
        "DOWNLOAD_DELAY": 0.5,
        # "CONCURRENT_REQUESTS_PER_DOMAIN": 2
    }

    def parse(self, response):
        selsector = Selector(response)
        print(response)
        xq = BookDetail()
        find_all = selsector.xpath('//*[@class="ListChapter"][last()]/ul/li/a')
        xq['bname'] = selsector.xpath('//*[@class="book_title"]/h1/text()').extract_first()
        xq['muser'] = selsector.xpath('//*[@class="author"]/text()').extract_first().replace('\xa0', '')
        yield xq
        num = 0
        for section in find_all:
            num += 1
            CName = section.xpath('.//text()').extract_first()
            href = section.xpath('.//@href').extract_first()
            TUrl = response.urljoin(href)
            TReKey = TUrl.split('/')
            TReKey[4] = 'txtt5551'
            CUrl = '/'.join(TReKey)
            request = scrapy.Request(CUrl, callback=self.parse_detail, meta={'num': num, 'CName': CName})
            yield request

    def parse_detail(self, response):
        xzbq = Selector(response)
        # huan= xzbq.xpath('//*[@id="chapter_title"]/h1/text()').extract()
        # tconn = xzbq.xpath('//*[@id="chapter_content"]/text()').extract()
        # conn = "\n".join(tconn)
        # cont = "\n".join(huan) #{'a','b','c'} -> a-b-c
        ChapterCon = xzbq.xpath('.//text()').extract()
        item = EbookItem()
        item['num'] = response.meta['num']
        item['ChaterNa'] = response.meta['CName']
        item['ChaterCo'] = ChapterCon
        yield item
