# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from GetKindleBook.items import EbookItem,BookDetail
import os

class GetkindlebookPipeline(object):
    def __init__(self):
        self.file = open('biquge_tmp.txt', 'w', encoding='utf-8')
        self.bookname = ""
        self.neir_list = []

    def process_item(self, item, spider):
        # print(item)
        # self.neir_list.append(item)
        if isinstance(item, BookDetail):
            self.bookname = item['bname'] + "-" + item['muser']
            return item
        else:
            self.neir_list.append(item)
            return item

    def close_spider(self, spider):
        list_sorted = sorted(self.neir_list, key=lambda x: x['num'])
        # print(list_sorted)
        for s in list_sorted:
            self.file.write(s['ChaterNa']+"\n")
            self.file.write('\n'.join(s['ChaterCo']).replace('\xa0', '')+"\n")
        self.file.close()
        try:
            os.rename('biquge_tmp.txt', self.bookname+".txt")
            #TODO 移动文件到指定目录
        except:
            print("Error:Rename biquge_tmp.txt Filed!")