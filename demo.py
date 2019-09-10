# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['aron.com']
    start_urls = ['http://aron.com/']

    def parse(self, response):
        pass
