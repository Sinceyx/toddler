# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface


class ToddlerSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        spider = cls()
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        return spider

    @staticmethod
    def process_spider_output(result):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for item in result:
            yield item

    @staticmethod
    def process_start_requests(start_requests):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for request in start_requests:
            yield request

    @staticmethod
    def spider_opened(spider):
        spider.logger.info('Spider opened: %s', spider.name)


class ToddlerDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        spider = cls()
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        return spider

    @staticmethod
    def process_response(response):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    @staticmethod
    def spider_opened(spider):
        spider.logger.info('Spider opened: %s', spider.name)
