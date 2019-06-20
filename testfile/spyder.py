url='http://www.tianqihoubao.com/aqi/yichang-201809.html'
d=url[url.rindex('-')+5:url.rindex('.')]
u='http://www.tianqihoubao.com/aqi/yichang-2018{0}.html'
d=int(d)+1
dd= "{0:02d}".format(d)
next_url=u.format(dd)
print(next_url)