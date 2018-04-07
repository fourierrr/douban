# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MusicReviewItem(scrapy.Item):
    review_title = scrapy.Field()
    review_content = scrapy.Field()
    review_author = scrapy.Field()
    review_music = scrapy.Field()
    review_time = scrapy.Field()
    review_url = scrapy.Field()