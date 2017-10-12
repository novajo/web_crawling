import requests
from scrapy import Selector


url = 'https://tieba.baidu.com/f?kw=%E9%98%BF%E6%A3%AE%E7%BA%B3&ie=utf-8&pn=0'
r = requests.get(url)
print (r.status_code)
sel = Selector(text=r.content, type='html')
# print r.content
xpath = sel.xpath('//li[@class=" j_thread_list clearfix"]//span[@class="frs-author-name-wrap"]/a/text()').extract()
n = 0
for x in xpath:
    n += 1
    print (x)
    print (n)