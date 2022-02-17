
import scrapy
from scrapy import Selector, Request

from toddler.items import HouseInfoItem, AgentInfoItem

HOST = 'http://luton.com.au/'


class LutonSpider(scrapy.Spider):
    name = 'luton'
    allowed_domains = ['luton.com.au']
    start_urls = [HOST]

    def parse(self, response):
        selector = Selector(response)
        properties_for_sale_restful_path = ''.join(selector.xpath('//*[@id="site-header"]/div[2]/nav/ul/li[1]/ul/li[1]/a/@href').extract())
        properties_for_sale_url = HOST + properties_for_sale_restful_path
        yield Request(properties_for_sale_url, callback=self.__parse_house_list)

        properties_for_lease_restful_path = ''.join(
            selector.xpath('//*[@id="site-header"]/div[2]/nav/ul/li[3]/ul/li[1]/a/@href').extract())
        properties_for_lease_restful_url = HOST + properties_for_lease_restful_path
        yield Request(properties_for_lease_restful_url, callback=self.__parse_house_list)

    def __parse_house_list(self, response):
        selector = Selector(response)
        listing_detail_urls = selector.xpath('/html/body/div[1]/main/section[2]/article/div/div/ul/li/div/a/div[2]/address/meta/@content').extract()
        for detail_url in listing_detail_urls:
            yield Request(''.join(detail_url), callback=self.__parse_house_detail)
        next_page_path = ''.join(selector.xpath('/html/body/div[1]/main/section[2]/article/div/div/div[2]/div/div[2]/a[2]/@href').extract())
        if '#' != next_page_path:
            yield Request(HOST + next_page_path, callback=self.__parse_house_list)

    def __parse_house_detail(self, response):
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
            agent_list.append(dict(agent_item))

        item['agent_info'] = agent_list
        yield item
