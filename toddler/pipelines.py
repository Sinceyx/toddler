# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import re

from toddler.items import HouseInfoItem


class ToddlerPipeline:

    def __init__(self):
        self.file = None

    def open_spider(self, spider):
        self.file = open('../output/house_info.jsonl', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def __state_name_filter(self, full_address: str):
        state_name_reject_list = ['NSW']
        state_name = re.compile('([A-Z]{2,})[\s]+[0-9]{4}$').search(full_address).groups(1)[0]
        if state_name not in state_name_reject_list:
            return True

    def __listing_type_filter(self, listing_type: str):
        listing_type_access_list = ['FOR SALE', 'FOR LEASE']
        if listing_type.upper() in listing_type_access_list:
            return True

    def __to_filter(self, item):
        return self.__listing_type_filter(item['listing_type']) and self.__state_name_filter(item['full_address'])

    def process_item(self, item, spider):
        if isinstance(item, HouseInfoItem):
            if self.__to_filter(item):
                self.file.write(json.dumps(dict(item)) + '\n')
                return item


