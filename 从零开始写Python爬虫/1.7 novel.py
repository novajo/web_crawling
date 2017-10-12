# -*- coding: utf-8 -*-
import requests
from scrapy import Selector
import csv


def get_sel(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    # print(r.status_code)
    sel = Selector(text=r.content, type='html')
    return sel


list_title = []
list_link = []
seed_url = 'http://www.qu.la/paihangbang/'
sel = get_sel(seed_url)
for se in sel.xpath("//div[contains(@class, 'index_toplist')]//div[contains(@id, 'con') and contains(@id, 'g_1')]//li/a[starts-with(@href, '/book/')]"):
    title = se.xpath("text()").extract()[0]
    link = se.xpath("@href").extract()[0]
    # print(str(title)+" http://www.qu.la/paihangbang"+str(link))
    if title not in list_title:
        list_title.append(title)
        list_link.append(link)

try:
    with open('novel_list.csv', 'w', newline='') as csvfile:
        fieldnames = ["title", "link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, len(list_title)):
            # print(list_title[i])
            writer.writerow({'title': list_title[i], 'link': (seed_url+list_link[i])})
        csvfile.close()
except PermissionError as e:
    print('Permission Denied')



