# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import FlaskDocItem

class FlaskSpider(CrawlSpider):
    name = 'flask'
    #allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/0.12/']
    rules = (
        Rule(
            LinkExtractor(allow='http://flask.pocoo.org/docs/0.12/.*'),
            callback = 'parse_item',
            follow = True
            ),       
    )

    def parse_item(self, response):
        yield FlaskDocItem({
            'url':response.url,
            'text':' '.join(response.css('::text').extract())
            })

       # yield item
