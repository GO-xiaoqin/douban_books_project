<!--
 * @Author: your name
 * @Date: 2020-04-10 21:32:05
 * @LastEditTime: 2020-04-11 13:22:52
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \git_project\douban_books_project\README.md
 -->

# 分布式豆瓣读书

关于豆瓣读书这个网站算是我的启蒙网站吧，从刚开始的少量数据爬取，到现在的增量数据爬取，从最初的被封IP，到如今依旧被封IP，哈哈哈，主要是穷，穷的响叮当。。

## 项目注意点

* 这个爬虫是基于RedisSpider继写的；
* 在settings里面的一些数据库设置，这里我的数据库没有密码如果侥幸被某位拿去运行可别存到我的盘里了；
* 我存储的是mongodb，如果要更改可以在pipelines里面更改；
* middlewares里面加了一个User-Agent请求池，效果可以，有条件的话建议加上代理IP，这样这个网站就可以随心随欲了不是，哈哈哈哈；
* 我实在Windows编的代码，放到Ubuntu运行的，因为是python所以没有太多的条件苛刻，该有的模块装上python3直接运行run.py文件即可；
* 其他没有太多注意点比较简单的小程序，练手记录一下！！！

## 项目部署

关于这个标签非常有必要讲一下，毕竟身为电脑小白的我也是要吐槽一下生活嘛，那么为什么会吐槽项目部署呢，这里小编是一个正在找工作的IT萌新，使用scrapy快半年了，一般都是自学，在网上看一些大牛们的博客讨生活，哈哈哈，这天本以为幸运女神会眷顾与我，投的简历终于有人肯面试我了，感觉开心无比，就约了电话面试，挺好的，可是当我面试的时候，面试官一顿连环问给问懵了，哈哈哈，我承认我有点菜了，第一次感觉到还是不够努力，印象最深的当时面试官问了一个分布式怎么部署，我当时在心里想这都是网上自己学野路子出来的，这怎么回答，有没有经验，哎，这也太难了，结结巴巴没有达上来，挂了电话自己这个恨呀，前几天刚看的内容就不会了，哎，没办法后悔是后悔，这不抓紧补一个简单分布式回想一些，这里算是我自己在没人的地方偷偷的吐槽一下自己和生活吧。

下面说一下分布式部署，最少保证有两个服务器以上，保证其中一台为主，另外的为从，在主机redis开放端口及网络，利用redis的去重和内存化储存，基于scrapy-redis组件，在settings设置组件的调度器，因为scrapy每一个项目有一个单独的调度器，设置组件的调度器，就可以达到共享URL队列，一个待爬取队列，一个爬取过的队列，以及URL去重，爬虫部分的的继承类也就变成了RedisSpider类、RedisCrawlSpider类这样代码部分就搭建完成，把代码搭建到每个服务器，就可以跑动起来了，当然有一个注意点如果要item存储到redis就要在settings设置pipelines。

关于项目部署我会说的只有这些也不知道说的对不对，如果有错，欢迎指正，热爱学习的IT萌新。。。。