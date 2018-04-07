# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-04-05 20:15:12
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-04-07 15:05:56


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from douban.items import MusicReviewItem
from scrapy import log

import re


class ReviewSpider(CrawlSpider):
    name = 'review'
    allowed_domains = ['music.douban.com']
    start_urls = ['https://music.douban.com/subject/1406522/']
    rules = (
        Rule(LinkExtractor(allow=r"/subject/\d+/reviews$")),
        Rule(LinkExtractor(allow=r"/subject/\d+/reviews\?sort=time$")),
        Rule(LinkExtractor(allow=r"/subject/\d+/reviews\?sort=time\&start=\d+$")),
        Rule(LinkExtractor(allow=r"/subject/\d+/reviews\?start=\d+$")),
        Rule(LinkExtractor(allow=r"/review/\d+/$"), callback="parse_review", follow=True),
    )

    def parse_review(self, response):
        try:
            item = MusicReviewItem()
            item['review_title'] = "".join(response.xpath('//*[@property="v:summary"]/text()').extract())
            content = "".join(
                response.xpath('//*[@id="link-report"]/div[@property="v:description"]/text()').extract())
            item['review_content'] = content.lstrip().rstrip().replace("\n", " ")
            if len(item['review_content'])<2:
                item['review_content']="".join(
                response.xpath('//*[@id="link-report"]/div[@property="v:description"]/p/text()').extract())
            item['review_author'] = "".join(response.xpath('//*[@property = "v:reviewer"]/text()').extract())
            item['review_music'] = "".join(response.xpath('//*[@class="main-hd"]/a[2]/text()').extract())
            item['review_time'] = "".join(response.xpath('//*[@class="main-hd"]/p/text()').extract())
            item['review_url'] = response.url
            yield item
        except Exception as error:
            log(error)