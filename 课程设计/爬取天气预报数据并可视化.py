import time, requests, re
import pandas as pd
from lxml import etree

# https://blog.csdn.net/u013337691/article/details/51894453

url = 'http://www.tianqihoubao.com/aqi/yichang.html'
headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36", }

response = requests.get(url, headers=headers)
html = response.text
response = etree.HTML(html)

url_list = response.xpath('//div[@class="box p"]//a/@href')
for url in url_list:
    url = 'http://www.tianqihoubao.com' + url

    # print(url)
    # url='http://www.tianqihoubao.com/aqi/hangzhou-201810.html'

    data = pd.read_html(url, header=0, encoding='gbk')[0]
    print(data)
    time.sleep(1)
