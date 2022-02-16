# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import json

import scrapy
from scrapy import Field


class ToddlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HouseInfoItem(scrapy.Item):
    agent_info = Field(serializer=json)
    listing_type = Field()
    full_address = Field()
    url = Field()


class AgentInfoItem(scrapy.Item):
    email = Field()
    name = Field()
