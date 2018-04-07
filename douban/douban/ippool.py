# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-04-05 23:30:48
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-04-07 12:16:53
# -*- coding: utf-8 -*-
import random
# 导入settings.py中的IPPOOL
from .settings import IPPOOL
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware


class ippool(HttpProxyMiddleware):

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        ip = random.choice(IPPOOL)
        print("当前使用IP是："+ ip)
        request.meta["proxy"] = "https://"+ip