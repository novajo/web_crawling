# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem


class KdlspiderSpider(scrapy.Spider):
    name = 'kdlspider'
    allowed_domains = ['kuaidaili.com']
    start_urls = []
    for i in range(1, 6):
        list_i = 'http://www.kuaidaili.com/free/inha/'+str(i)+'/'
        start_urls.append(list_i)

    def parse(self, response):
        item = ProxyItem()

        ip_lists = response.xpath('//tbody/tr')
        for li in ip_lists:
            # ip = li.xpath('/td[@data-title="IP"]/text()').extract()
            # port = li.xpath('/td[@data-title="PORT"]/text()').extract()
            ip = li.xpath('td[@data-title="IP"]/text()').extract_first()
            port = li.xpath('td[@data-title="PORT"]/text()').extract_first()
            # ip = li.xpath('td/text()').extract()[0]
            # port = li.xpath('td/text()').extract()[1]
            print('ip address is belowing')
            print(ip)
            print('port number is belowing')
            print(port)
            item['addr'] = ip+':'+port
            yield item
