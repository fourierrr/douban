# -*- coding: utf-8 -*-
# @Author: Nessaj
# @Date:   2018-04-06 22:58:41
# @Last Modified by:   Nessaj
# @Last Modified time: 2018-04-06 23:14:07

from OpenSSL import SSL
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory
class CustomContextFactory(ScrapyClientContextFactory):
    """
    Custom context factory that allows SSL negotiation.
    """
    def __init__(self,method=SSL.SSLv23_METHOD):
        # Use SSLv23_METHOD so we can use protocol negotiation
        self.method = method