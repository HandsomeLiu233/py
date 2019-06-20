import scrapy
import re

class MySpider(scrapy.spiders.Spider):
    name='spiderYichangGuishi'
    start_urls=['http://bbs.tianya.cn/post-16-1126849-1.shtml']
    def parse(self,response):
        content=[]
        for i in response.xpath('//div'):
            if i.xpath('@_hostid').extract()==['13357319']:
                for j in i.xpath('div//div'):
                    c=j.xpath('text()').extract()
                    g=lambda x:x.strip('\n\r').replace('<br>','\n').replace('|','')
                    c='\n'.join(map(g,c)).strip()
                    content.append(c)
        with open('result.txt','a+',encoding='utf8') as fp:
            fp.writelines(content)

        url=response.url
        d=url[url.rindex('-')+1:url.rindex('.')]

        u='http://bbs.tianya.cn/post-16-1126849-{0}.shtml'
        next_url=u.format(int(d)+1)
        try:
            yield scrapy.Request(url=next_url,callback=self.parse)

        except:
            pass


