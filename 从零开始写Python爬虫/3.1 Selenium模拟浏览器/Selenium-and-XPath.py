# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import requests
from scrapy import Selector


def get_sel(url, UA):
    headers = {
        'User-Agent': UA
    }
    r = requests.get(url, headers=headers)
    # print(r.status_code)
    selector = Selector(text=r.text, type='html')
    return selector

# 设置userAgent
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
UA = random.choice(user_agent_list)
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = UA

browser = webdriver.PhantomJS(executable_path=r"E:\phantomjs\bin\phantomjs.exe", desired_capabilities=dcap)
# browser.set_window_size(1920, 1080)
browser.set_window_size(1440, 900)


seed = 'https://www.pilz.com'
# url = 'https://www.pilz.com/zh-CN/eshop'
eshop_sel = get_sel(seed+'/zh-CN/eshop', UA)
prod_links = eshop_sel.xpath('//a[@class="btn btn-link" and starts-with(@href, "/zh-CN/eshop/00")]/@href').extract()
for prod_link in prod_links:
    # print(seed + prod_link)
    sel = get_sel(seed + prod_link, UA)
    teaser_links = sel.xpath("//ul[@class='link-list']//a[text()='元件']/@href").extract()
    for teaser_link in teaser_links:
        # 去除软件授权类产品
        if 'Licence' not in teaser_link:
            components_lists_link = seed + teaser_link
            # print('this is component lists link')
            # print(components_lists_link)
            material_lists_sel = get_sel(components_lists_link, UA)
            # 判断元件列表是否只有一页
            pagenavigation = material_lists_sel.xpath('//ul[@class = "pagination"]//span[text() = "»"]/ancestor::li/preceding-sibling::li[1]//a/text()').extract_first()
            if pagenavigation is None:
                # only one page
                pagenavi = 1
            else:
                # multiple pages
                pagenavi = int(pagenavigation)

            for p in range(1, pagenavi + 1):
                if p == 1:
                    browser.get(components_lists_link)
                    print('crawling page {}, click next page button and waiting for 3 seconds'.format(str(p)))
                    browser.implicitly_wait(3)
                    # agent = browser.execute_script("return navigator.userAgent")
                    # print(agent)
                else:
                    navi_button = browser.find_element_by_xpath('//span[text() = "»"]')
                    navi_button.click()
                    print('crawling page {}, click next page button and waiting for 3 seconds'.format(str(p)))
                    browser.implicitly_wait(3)

                material_links = browser.find_elements_by_xpath('//div[contains(@class, "c-3")]//a[@rel="nofollow"]')
                for material_link in material_links:
                    single_material_link = material_link.get_attribute('href')
                    # print('this is single page')
                    print(single_material_link)
                    sel = get_sel(single_material_link, UA)
                    download_manual = sel.xpath('//a/@href').extract()
                    for d in download_manual:
                        print(d)

                if p == pagenavi:
                    pass
                    # browser.close()
                    # print('current material is done. browser is closed')













