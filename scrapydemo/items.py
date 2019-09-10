# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    job = scrapy.Field()
    location = scrapy.Field()
    publish_time = scrapy.Field()
    salary = scrapy.Field()
    requirement = scrapy.Field()
