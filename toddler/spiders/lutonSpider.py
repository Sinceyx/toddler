import scrapy
from scrapy import Selector, Request

from toddler.items import HouseInfoItem, AgentInfoItem

host = 'http://luton.com.au/'


class LutonSpider(scrapy.Spider):
    name = 'luton'
    allowed_domains = ['luton.com.au']
    start_urls = [host]

    def parse(self, response):
        selector = Selector(response)
        properties_for_sale_restful_path = ''.join(selector.xpath('//*[@id="site-header"]/div[2]/nav/ul/li[1]/ul/li[1]/a/@href').extract())
        properties_for_sale_url = host + properties_for_sale_restful_path
        yield Request(properties_for_sale_url, callback=self.parse_for_sale_list)

    def parse_for_sale_list(self, response):
        selector = Selector(response)
        listing_detail_urls = selector.xpath('/html/body/div[1]/main/section[2]/article/div/div/ul/li/div/a/div[2]/address/meta/@content').extract()
        for detail_url in listing_detail_urls:
            yield Request(''.join(detail_url), callback=self.parse_for_sale_house_detail)

    def parse_for_sale_house_detail(self, response):
        item = HouseInfoItem()
        selector = Selector(response)
        address_xpath = selector.xpath('/html/body/div[1]/main/section[2]/div/h1')
        street_address = ''.join(address_xpath.xpath('./span/text()').extract())
        suburb = ''.join(address_xpath.xpath('./small/span[1]/text()').extract())
        address_region = ''.join(address_xpath.xpath('./small/span[3]/text()').extract())
        postal_code = ''.join(address_xpath.xpath('./small/span[2]/text()').extract())
        item['full_address'] = street_address + ',' + suburb + ',' + address_region + ' ' + postal_code
        item['url'] = response.url
        item['listing_type'] = ''.join(selector.xpath('/html/body/div[1]/main/section[2]/article/div/div[2]/h2/text()').extract())

        agent_list_xpath = selector.xpath("/html/body/div[1]/main/section[2]/article/div/div[1]/ul/li")
        agent_list = []
        for agent_xpath in agent_list_xpath:
            agent_item = AgentInfoItem()
            agent_item['name'] = ''.join(agent_xpath.xpath('./div/div/div/span/text()').extract())
            agent_item['email'] = ''.join(agent_xpath.xpath('./div/div/dl/dd[1]/a/text()').extract())
            agent_list.append(agent_item)

        item['agent_info'] = agent_list
        yield item