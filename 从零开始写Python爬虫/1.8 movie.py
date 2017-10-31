# -*- coding: utf-8 -*-
from scrapy import Selector
import requests


def get_sel(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    # print(r.status_code)
    selector = Selector(text=r.text, type='html')
    return selector


def download_img(url, name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    with open('c:/Users/wniu/Desktop/img/' + name + '.png', 'wb+') as f:
        f.write(r.content)


def get_Movies():
    url = 'http://dianying.2345.com/top/'
    sel = get_sel(url)
    section = sel.xpath('//ul[@class="picList clearfix"]/li')
    #title = section.xpath('//span[@class="sTit"]/a/text()').extract()
    for s in section:
        # print(s)
        title = s.xpath('div[@class="txt"]/p[@class="pTit"]/span[@class="sTit"]/a/text()').extract_first()
        starrings = s.xpath('div[@class="txt"]/p[@class="pActor"]/a/text()').extract()
        intro = s.xpath('div[@class="txt"]/p[@class="pTxt pIntroShow"]/text()').extract_first()
        img_url = "http:"+s.xpath('div[@class="pic"]/img/@src').extract_first()
        download_img(img_url, title)
        # if title is not None:
        print("片名: "+title)
        print("主演: ")
        for starring in starrings:
            print(starring)
        print(intro)
        print('----------------------------------------------')


get_Movies()
