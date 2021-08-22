# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TwentyfourhourfitnessclubItem(scrapy.Item):
    store_name = scrapy.Field()
    address1 = scrapy.Field()
    address2 = scrapy.Field()
    address3 = scrapy.Field()
    phone_number = scrapy.Field()
