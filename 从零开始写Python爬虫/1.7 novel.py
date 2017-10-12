# -*- coding: utf-8 -*-
import requests
import datetime
from scrapy import Selector
import csv


def get_sel(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    print(r.status_code)
    sel = Selector(text=r.content, type='html')
    return sel


seed_url = 'http://www.qu.la/paihangbang/'
sel = get_sel(seed_url)
cnt = 0
for se in sel.xpath("//div[contains(@class, 'index_toplist')]//div[contains(@id, 'con') and contains(@id, 'g_1')]//li/a[starts-with(@href, '/book/')]"):
    text = se.xpath("text()").extract()[0]
    link = se.xpath("@href").extract()[0]
    print(str(text)+" http://www.qu.la/paihangbang"+str(link))
    cnt += 1
print(cnt)
'''
for se in sel.xpath('//div[@class="topbooks" and @style="display: block;"]/ul/li/a'):
    s = Selector(text=se.extract(), type='html')
    internal_link = s.xpath('//@href').extract_first()
    title = s.xpath('//@title').extract_first()
    download_link = seed_url + str(internal_link)
    with open('novel_list.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.write(title.encode('utf-8'))
        writer.write(download_link)
        csvfile.close()
        '''




