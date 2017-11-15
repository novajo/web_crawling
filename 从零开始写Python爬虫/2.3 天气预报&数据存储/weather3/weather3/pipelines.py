# -*- coding: utf-8 -*-
# from weather3.weather_mysql import insert
import json
import os
import codecs
# import pandas as pd

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Weather3Pipeline_json(object):
    def process_item(self, item, spider):
        # date = item['date']
        # week = item['week']
        # temperature = item['temperature']
        # weather = item['weather']
        # wind = item['wind']
        # city = item['city']

        # base_dir = os.getcwd()
        filename = 'weather.json'
        with codecs.open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)

        # insert(date, week, temperature, weather, wind, city)
        return item
