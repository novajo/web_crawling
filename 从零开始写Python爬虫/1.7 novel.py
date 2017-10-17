# -*- coding: utf-8 -*-
import requests
from scrapy import Selector
import csv
import time
import random


def get_sel(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    # print(r.status_code)
    selector = Selector(text=r.content, type='html')
    return selector


def get_txt(book_name, section_name, section_url):
    # 根据易获取的章节链接，读取每个章节的具体文字内容
    txt_sel = get_sel(section_url)
    entire_section_txt = ''
    for t in (txt_sel.xpath("//div[@class = 'content_read']//div[@id = 'content']/text()").extract())[:-3]:
        # 获取列表最后3个元素为广告，添加-3去广告
        print(t)
        entire_section_txt += (t + '\n')
    try:
        with open('{}.txt'.format(book_name), 'a', encoding='utf-8') as f:
            f.write(section_name + '\n\n')
            f.write(entire_section_txt)
            f.close()
        print('当前小说：{}，当前章节:{} 已经下载完毕'.format(book_name, section_name))
        delay = random.uniform(3, 10)
        time.sleep(delay)
        print('sleeping for {}seconds'.format(delay))
    except:
        print('something wrong')


def get_section(book_name, book_url):
    # 根据获取的小说链接，读取每本小说的章节链接
    section_sel = get_sel(book_url)
    for c_se in section_sel.xpath("//div[@class = 'box_con']/div[@id = 'list']//dd/a"):
        # 根据小说链接，遍历章节
        section_title = c_se.xpath("text()").extract()[0]
        section_content_link = "http://www.qu.la/paihangbang"+str(c_se.xpath("@href").extract()[0])
        print(str(section_title)+" "+section_content_link)
        get_txt(book_name, section_title, section_content_link)
        # 嵌套读取文本内容功能


list_title = []
list_link = []
seed_url = 'http://www.qu.la/paihangbang/'
sel = get_sel(seed_url)
for se in sel.xpath("//div[contains(@class, 'index_toplist')]//div[contains(@id, 'con') and contains(@id, 'g_1')]//li/a[starts-with(@href, '/book/')]"):
    # 根据种子域名，遍历小说排行榜，使用con与g_1的判定抓取月度榜单
    title = se.xpath("text()").extract()[0]
    link = se.xpath("@href").extract()[0]
    external_link = "http://www.qu.la/paihangbang"+str(link)
    if link not in list_link:
        # 使用唯一链接地址实现去重
        list_title.append(title)
        list_link.append(link)
        print(str(title)+" ------------------ ")
        get_section(title, external_link)
        # 嵌套获取章节链接功能

'''
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
'''


