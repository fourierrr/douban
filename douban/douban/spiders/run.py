# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-04-05 16:06:31
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-04-07 15:11:48

from scrapy import cmdline
cmdline.execute("scrapy crawl review -o review.json".split())