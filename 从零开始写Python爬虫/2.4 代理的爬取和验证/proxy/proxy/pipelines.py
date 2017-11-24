# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'xicispider':
            open('xici_proxy.txt', 'a').write(item['addr'] + '\n')
        elif spider.name == 'kdlspider':
            open('kdl_proxy.txt', 'a').write(item['addr']+'\n')
        return item
