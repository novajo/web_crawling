# -*- coding: utf-8 -*-
import scrapy
from weather3.items import Weather3Item


class ShtianqiSpider(scrapy.Spider):
    name = 'SHtianqi'
    allowed_domains = ['tianqi.com']
    start_urls = []
    citys = ['shanghai', 'suzhou', 'hangzhou']
    for city in citys:
        start_urls.append('https://www.tianqi.com/{}/'.format(city))

    def parse(self, response):
        items = []
        # sevenday = response.xpath('//div[@class="day7"]')
        for i in range(0, 7):
            item = Weather3Item()
            item['date'] = response.xpath('//div[@class="day7"]/ul[@class="week"]/li/b/text()').extract()[i]
            item['week'] = response.xpath('//div[@class="day7"]/ul[@class="week"]/li/span/text()').extract()[i]
            item['img'] = response.xpath('//div[@class="day7"]/ul[@class="week"]/li/img/@src').extract()[i]

            item['temperature'] = response.xpath('//div[@class="day7"]/div[@class="zxt_shuju"]/ul/li/span/text()').extract()[i]
            item['weather'] = response.xpath('//div[@class="day7"]/ul[contains(@class, "txt2")]/li/text()').extract()[i]
            item['wind'] = response.xpath('//div[@class="day7"]/ul[@class="txt"]/li/text()').extract()[i]
            item['city'] = response.xpath('//dd[@class="name"]/h2/text()').extract_first()
            items.append(item)
        return items

