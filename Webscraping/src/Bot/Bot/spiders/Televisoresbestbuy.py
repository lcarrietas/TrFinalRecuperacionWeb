# -*- coding: utf-8 -*-
import scrapy


class TelevisoresbestbuySpider(scrapy.Spider):
    name = 'Televisoresbestbuy'
    allowed_domains = ['https://www.bestbuy.com/site/tvs/all-flat-screen-tvs/abcat0101001.c?id=abcat0101001']
    start_urls = ['http://https://www.bestbuy.com/site/tvs/all-flat-screen-tvs/abcat0101001.c?id=abcat0101001/']

    def parse(self, response):
        pass
