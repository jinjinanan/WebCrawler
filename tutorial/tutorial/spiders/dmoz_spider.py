import scrapy
from ..items import DmozItem

class DmozSpider(scrapy.spiders.Spider):
    # 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
    name = 'dmoz'
    #
    allowed_domains = ['dmoz.org']
    # 包含了Spider在启动时进行爬取的url列表。
    # 因此，第一个被获取到的页面将是其中之一。
    # 后续的URL则从初始的URL获取到的数据中提取
    start_urls = [
        'http://dmoz-odp.org/Computers/Programming/Languages/Python/Books/',
        'http://dmoz-odp.org/Computers/Programming/Languages/Python/Resources/'
    ]

    def parse(self,response):

        for sel in response.css('.title-and-desc'):
            item = DmozItem()
            item['title'] = sel.xpath('a/div/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('div/text()').extract()
            yield item
