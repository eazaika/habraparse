# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from habr.items import HabrItem

class HabrspiderSpider(CrawlSpider):
    name = 'HabrSpider'
    allowed_domains = ['habrahabr.ru']
    start_urls = ['https://habr.ru/']

    rules = (
        Rule(LinkExtractor(allow=('/page\d+/',)), callback='parse_page'),
    )

    def parse_start_url(self, response):
        return self.parse_page(response)

    def parse_page(self, response):
        root = Selector(response)
        posts = root.xpath('//article[@class="post post_preview"]')
        for post in posts:
            item = HabrItem()
            item['title'] = post.xpath(\
                './/h2[@class="post__title"]/a/text()').extract()[0]
            item['author'] = post.xpath(\
                './/header[@class="post__meta"]/a/span/text()').extract()[0]
            item['stars'] = post.xpath(\
                './/footer[@class="post__footer"]/ul/li/div/span/text()').extract()[0]
            yield item
