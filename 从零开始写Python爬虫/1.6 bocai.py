# -*- coding: UTF-8 -*-

import requests
import datetime
from scrapy import Selector

def get_sel(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    print r.status_code
    sel = Selector(text=r.content, type='html')
    return sel


today = datetime.date.today()
print today
print type(today)
print str(today)
sel = get_sel('http://trade.500.com/jczq/')

for s in sel.xpath('//tbody/tr[@pdate="2017-09-24"]/text()').extract():
    print s

'''
for s in get_sel('http://trade.500.com/jczq/').xpath('//tbody/tr[@pdate="2017-09-24"]'):
    home_team = s.xpath('/td[@class="left_team"]/a/text()').extract()
    away_team = s.xpath('//td[@class="right_team"]/a/text()').extract()
    odds = s.xpath('//td/div[@class="bet_odds"]/span/text()').extract()
    print home_team
    print away_team
    print odds
    '''
