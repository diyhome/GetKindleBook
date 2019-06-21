# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class GetkindlebookPipeline(object):
    def __init__(self):
        self.file = open('琼明神女录.txt', 'w', encoding='utf-8')
        self.neir_list = []

    def process_item(self, item, spider):
        # print(item)
        self.neir_list.append(item)
        return item

    def close_spider(self, spider):
        list_sorted = sorted(self.neir_list, key=lambda x: x['num'])
        # print(list_sorted)
        for s in list_sorted:
            self.file.write(s['ChaterNa']+"\n")
            self.file.write('\n'.join(s['ChaterCo']).replace('\xa0', '')+"\n")
        self.file.close()