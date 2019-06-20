import scrapy
import pandas as pd
import string


class MySpider(scrapy.spiders.Spider):
    name='Stq'
    start_urls=['http://www.tianqihoubao.com/aqi/yichang-201801.html']
    def parse(self,response):
        url=response.url
        data = pd.read_html(url, header=0, encoding='gbk')[0]
        print(data)
        d=url[url.rindex('-')+5:url.rindex('.')]
        u='http://www.tianqihoubao.com/aqi/yichang-2018{0}.html'
        d = int(d) + 1
        dd = "{0:02d}".format(d)
        next_url=u.format(dd)
        if dd=='02':
            data.to_csv('D:/result.csv', mode='a', header=True, encoding="gbk")
        else:
            data.to_csv('D:/result.csv', mode='a', header=False, encoding="gbk")


        try:
            yield scrapy.Request(url=next_url,callback=self.parse)

        except:
            dd>3
            pass