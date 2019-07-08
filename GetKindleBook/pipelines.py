# -*- coding: utf-8 -*-

import os
import shutil

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from GetKindleBook.items import BookDetail


class GetkindlebookPipeline(object):
    def __init__(self):
        self.dftName = "tmp.txt"
        self.file = open(self.dftName, 'w', encoding='utf-8')
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
            self.file.write(s['ChaterNa'] + "\n")
            self.file.write('\n'.join(s['ChaterCo']).replace('\xa0', '') + "\n")
        self.file.close()
        FileName = self.bookname + ".txt"
        try:
            os.rename(self.dftName, FileName)
        except:
            print("Error:Rename %self.dftName Filed!")
        try:
            shutil.move(FileName, "save")
        except:
            print("Faild:Move %FileName faild!")
