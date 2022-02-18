"""
    Item is a return type as spider parse function,and as a parameter to pipeline process_item
"""

import json

import scrapy
from scrapy import Field


class HouseInfoItem(scrapy.Item):
    """
        House information structure of luton.com.au main products
    """
    agent_info = Field(serializer=json)
    listing_type = Field()
    full_address = Field()
    url = Field()


class AgentInfoItem(scrapy.Item):
    """
        Agent information structure . Its value is as the value to HouseInfoItem['agent_info']
    """
    email = Field()
    name = Field()
