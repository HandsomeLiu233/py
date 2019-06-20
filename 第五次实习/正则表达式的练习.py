import re


'''
textstr1='asdjoi3pop123njn6pn343p'
textstr2='A8juyG85GHNBVT97JNMjhg65'

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)
'''
url='http://bbs.tianya.cn/post-16-1126849-1.shtml'
d=re.findall('\-.\.',url)
s=int(d[0][1])
print(s)
