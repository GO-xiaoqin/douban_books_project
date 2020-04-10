'''
@Author: your name
@Date: 2020-04-05 14:35:11
@LastEditTime: 2020-04-10 14:35:05
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\douban_books\douban_book_project\items.py
'''
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookProjectItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author_price = scrapy.Field()
    score = scrapy.Field()
    introduction = scrapy.Field()
