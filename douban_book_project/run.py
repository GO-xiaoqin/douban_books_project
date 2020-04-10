'''
@Author: your name
@Date: 2020-03-07 14:19:46
@LastEditTime: 2020-03-28 12:27:52
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \python\douban_books\douban_book_project\douban_book_project\run.py
'''
from scrapy import cmdline

cmd = 'scrapy crawl douban'
cmdline.execute(cmd.split())
