import requests
import time
from multiprocessing.dummy import Pool as ThreadPool 

dir_path = 'C:/nutbox/python/myscraping/web_crawling/从零开始写Python爬虫/2.4 代理的爬取和验证/proxy/'
alive_ip = []
pool = ThreadPool(850)

def test_alive(proxy):
    global alive_ip
    proxies = {'http': proxy}
    print('正在测试：{}'.format(proxies))
    try:
        r = requests.get('http://www.baidu.com', proxies=proxies, timeout=3)
        if r.status_code == 200:
            print('该代理：{} 测试成功'.format(proxy))
            print('\n')
            alive_ip.append(proxy)
    except:
        print('该代理：{} 已失效'.format(proxy))
        print('\n')


def Out_file(alive_ip=[]):
    global dir_path
    with open(dir_path + 'alive_ip.txt', 'a+') as f:
        for ip in alive_ip:
            f.write(ip + '\n')
        print('所有存活IP已写入文件！')

def test(filename='xici_proxy.txt'):
    with open(dir_path + filename, 'r') as f:
        lines = f.readlines()
        proxys = list(map(lambda x: x.strip(), [y for y in lines]))
        pool.map(test_alive, proxys)
    Out_file(alive_ip)

start = time.clock()
test('kdl_proxy.txt')
test('xici_proxy.txt')
end = time.clock()
print(end-start)