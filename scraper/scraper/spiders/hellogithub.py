# -*- coding: utf-8 -*-
import scrapy

from ..items import ArticleItem


class HellogithubSpider(scrapy.Spider):
    name = 'hellogithub'
    allowed_domains = ['hellogithub.com']
    start_urls = ['https://hellogithub.com/periodical/volume/32/']

    def parse(self, response):
        articles = response.css(".project-url")
        for article in articles:
            item = ArticleItem()
            item['title'] = article.css('.project-url::text').extract_first()
            # item['content'] = article.css('p::text').extract_first()
            yield item

        next = response.css('.pre a::attr("href")').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
