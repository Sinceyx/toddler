# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from toddler.items import HouseInfoItem


class ToddlerPipeline:

    def __init__(self):
        self.file = None

    def open_spider(self, spider):
        self.file = open('../output/house_info.jsonl', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, HouseInfoItem):
            line = json.dumps(dict(item)) + '\n'
            self.file.write(line)
        return item
