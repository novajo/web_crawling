# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem


class XicispiderSpider(scrapy.Spider):
    name = 'xicispider'
    allowed_domains = ['xicidaili.com']
    start_urls = []
    for i in range(1, 6):
        start_urls.append('http://www.xicidaili.com/nn/{}'.format(i))

    def parse(self, response):
        item = ProxyItem()
        lists = response.xpath('//tr[@class="odd" or @class=""]')
        for l in lists:
            ip = l.xpath('td/text()').extract()[0]
            port = l.xpath('td/text()').extract()[1]
            print('ip address is belowing')
            print(ip)
            print('port number is belowing')
            print(port)
            item['addr'] = ip+':'+port
            yield item
