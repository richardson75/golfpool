# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ResultsItem(scrapy.Item):
    tourn_id = scrapy.Field()
    url_id = scrapy.Field()
    player = scrapy.Field()
    place = scrapy.Field()
    payout = scrapy.Field(default = '0')

class RankItem(scrapy.Item):
    player3= scrapy.Field()
    rank = scrapy.Field()
    tourn_id = scrapy.Field()