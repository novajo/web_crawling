import requests
from scrapy import Selector
import random
import time



def get_sel(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers, timeout=5)
        selector = Selector(text=r.text, type='html')
        return selector
    except:
        print("error")


rest = 0
homepage = 'http://sh.lianjia.com/ershoufang/'
homepage_selector = get_sel(homepage)
districts = homepage_selector.xpath('//div[@class="location-child" and @id="plateList"]/div[@class="level1"]/a[@gahref!="district-nolimit"]/@href').extract()


seed_url = 'http://sh.lianjia.com'
for district in districts:
    district_url = seed_url + district
    district_sel = get_sel(district_url)
    areas = district_sel.xpath('//div[@class="location-child" and @id="plateList"]/div/div[@class="level2-item"]/a[@gahref!="plate-nolimit"]/@href').extract()
    for area in areas:
        print("area is " + str(area))
        area_home_url = seed_url + area
        area_sel = get_sel(area_home_url)
        total_pages = area_sel.xpath('//a[@gahref="results_totalpage"]/text()').extract()[0]
        for n in range(1, int(total_pages)+1):
            area_page_url = area_home_url + "d" + str(n)
            area_page_sel = get_sel(area_page_url)
            area_single_pages = area_page_sel.xpath('//ul[@class="js_fang_list"]/li/a[starts-with(@gahref, "results_click_order")]/@href').extract()
            for single_page in area_single_pages:
                single_page_url = seed_url + single_page
                single_page_sel = get_sel(single_page_url)
                rest += 1
                if rest >= 30:
                    rest = 0
                    sleep_seconds = random.uniform(1.0, 10.0)
                    print("sleeping in %d seconds" % sleep_seconds)
                    time.sleep(sleep_seconds)
                else:
                    pass
                # brief introduction  of a single house
                header_intro = single_page_sel.xpath('/html/body/section[@class="top-wrapper"]/header[@class="m-header"]/div[@class="content-wrapper"]/div[@class="header-row2"]/h1[@class="header-title"]/text()').extract()[0]
                # detail information of a single house
                basic_info = single_page_sel.xpath('//div[@class="content-main module-tb"]/div[@class="module-row"]')
                basic_info_column2 = basic_info.xpath('div[@class="module-col baseinfo-col2"]/ul[@class="baseinfo-tb"]/li/span[@class="item-cell"]/text()').extract()
                house_type = basic_info_column2[0]
                built_area = basic_info_column2[2]
                last_sell = basic_info_column2[4].strip()
                print(header_intro)
                print(house_type)
                print(built_area)
                print(last_sell)
                print(".........")

                basic_info_column3 = basic_info.xpath('div[@class="module-col baseinfo-col3"]/ul[@class="baseinfo-tb"]/li/span[@class="item-cell"]/text()').extract()
                room_floor = basic_info_column3[0]
                decoration_status = basic_info_column3[1]
                house_orientation = basic_info_column3[2].strip()
                property_type = basic_info_column3[4].strip()
                print(room_floor)
                print(decoration_status)
                print(house_orientation)
                print(property_type)
                print("______________")