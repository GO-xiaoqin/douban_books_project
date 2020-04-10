'''
@Author: your name
@Date: 2020-03-07 17:28:06
@LastEditTime: 2020-04-10 20:52:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\douban_books\douban_book_project\spiders\douban.py
'''
# -*- coding: utf-8 -*-
import scrapy
import sys
import os
sys.path.append(os.getcwd() + "\\douban_book_project")
from items import DoubanBookProjectItem
from scrapy_redis.spiders import RedisSpider


class DoubanSpider(RedisSpider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    # start_urls = ['https://book.douban.com/tag/']
    redis_key = 'douban_spider'

    def parse(self, response):
        # 进行数据分析，及详情页信息提取
        book_tags = response.xpath(
            "//div[@id='content']//b/../a/@href").extract()
        for book in book_tags:
            yield scrapy.Request(response.urljoin(book),
                                 callback=self.parse_items)

    def parse_items(self, response):
        # 对分类下的图书信息进行提取
        douban_item = DoubanBookProjectItem()
        books_xpath = response.xpath("//ul[@class='subject-list']//li")
        for li in books_xpath:
            douban_item['title'] = li.xpath(".//h2/a/text()").get()
            douban_item['author_price'] = li.xpath(".//div[@class='pub']/text()").get()
            douban_item['score'] = li.xpath(".//span[@class='rating_nums']/text()").get()
            douban_item['introduction'] = li.xpath(".//p/text()").get()
            yield douban_item
        # 稍后做下一页处理
        next_href = response.xpath('//span[@class="next"]/a/@href')
        if len(next_href) > 0:
            # 还有下一页
            next_href = next_href.get()
            yield scrapy.Request(response.urljoin(next_href),
                                 callback=self.parse_items)
        else:
            pass
