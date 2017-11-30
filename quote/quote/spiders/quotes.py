# -*- coding: utf-8 -*-
import scrapy

from quote.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        #print(response.text)
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first() #只查找一个内容
            tags = quote.css('.tags .tag::text').extract() #查找所有元素

            #对item进行赋值
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

            #提取下一页
        nextPage = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(nextPage) #生成完整的url
        yield scrapy.Request(url=url, callback=self.parse)

