# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider1(scrapy.Spider):
    name = 'golden1'
    allowed_domains = ['gold.com']
    start_urls = ['https://www.goldtoutiao.com/']

    def parse(self, response):

        item = response.xpath("//div[@class= 'articlelist-item_main']/a/text()")

        yield item

        print(item)







process = CrawlerProcess()
process.crawl(MySpider1)

process.start()
