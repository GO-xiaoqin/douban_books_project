'''
@Author: your name
@Date: 2020-03-08 12:45:40
@LastEditTime: 2020-04-10 20:30:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\douban_books\douban_book_project\pipelines.py
'''
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
import pymongo


class DoubanBookProjectPipeline(object):
    """
    ???????????
    """
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(
            host=spider.settings.get('MONGO_HOST'),
            port=spider.settings.get('MONGO_PORT'),
        )
        # ?????????????
        # self.client.admin.authenticate(
        #     settings['MINGO_USER'],
        #     settings['MONGO_PSW']
        #     )
        self.db = self.client[spider.settings.get('MONGO_DB')]  # ????????
        # ??collection???
        # self.coll = self.db[spider.settings.get('MONGO_COLL')]
        self.coll = self.db['douban_books']

    def process_item(self, item, spider):
        # ????
        author_price = [x.split() for x in item['author_price'].split("/")]
        # print(author_price)
        author = author_price[0]
        # print(author)
        pattern = re.compile(r'\[.*?\]|\(.*?\)')
        print(pattern.findall(author[0]))
        if len(author) and len(pattern.findall(author[0])) > 0:
            if author[0] == pattern.findall(author[0])[0]:
                author = author[0] + author[1]
        book = {}
        book['title'] = item['title'].split()[0]
        book['author'] = author
        book['price'] = author_price[-1] if len(author_price[-1]) > 0 else None
        book['introduction'] = item['introduction'].split()[0]
        self.coll.insert(book)  # ??????????,?????

        return item
