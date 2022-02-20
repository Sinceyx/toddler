import unittest
import os
from toddler.spiders.luton_spider import LutonSpider
from scrapy.http import TextResponse, Request


def fake_response_from_file(file_name, url=None):
	request = Request(url)
	if not file_name[0] == '/':
		response_dir = os.path.dirname(os.path.realpath(__file__))
		file_path = os.path.join(response_dir, file_name)
	else:
		file_path = file_name

	with open(os.path.realpath(file_path), 'r') as f:
		file_content = f.read()

	response = TextResponse(url=url, request=request, body=file_content.encode('utf-8'))
	return response


class LutonSpiderTest(unittest.TestCase):
	def test_parse(self):
		host = 'http://luton.com.au/'
		properties_for_sale_path = '/properties-for-sale'
		properties_for_lease_path = '/properties-for-rent'

		expected_for_sale_result = Request(host + properties_for_sale_path)
		expected_for_lease_result = Request(host + properties_for_lease_path)

		spider = LutonSpider()
		parse_result = spider.parse(response=fake_response_from_file('fake_response_from_luton_home_page.html', host))

		actual_result_for_sale = parse_result.__next__()
		self.assertEqual(expected_for_sale_result.url, actual_result_for_sale.url)

		actual_result_for_lease = parse_result.__next__()
		self.assertEqual(expected_for_lease_result.url, actual_result_for_lease.url)