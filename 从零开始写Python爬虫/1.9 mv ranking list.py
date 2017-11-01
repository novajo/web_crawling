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


def get_mv_ranking():
    D = {}
    url = 'http://vchart.yinyuetai.com/vchart/trends?area='
    area = ['ML', 'HT', 'US', 'KR', 'JP']
    for ar in area:
        scrap_url = url+ar
        print(scrap_url)
        sel = get_sel(scrap_url)
        section = sel.xpath('//ul[@id="rankList"]/li[@name="dmvLi"]/div[starts-with(@class, "infoBox")]')
        for s in section:
            score = s.xpath('div[@class="score_box"]/h3/text()').extract_first()
            # print(score)
            title = s.xpath('div[@class="mv_info"]/div[@class="info"]/h3/a[@class="mvname"]/text()').extract_first()
            D['score'] = score
            D['title'] = title
            print(D)


get_mv_ranking()

