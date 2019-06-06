# format的用法
def UseOfFormat():
    print('the number 1 is called {0:,},and it in hex is called {0:#x},the number 2 is called {1:,},and it in oct is {1:o}'.format(123,456))
    print('fxxk {you},It is son of a bixch.And It always fuck with {badguy} for {time1} hours'.format(you='xiaoming',badguy='xiaohong',time1='120'))
    position=('he','she','it')
    print('we all say {0[0]},and {0[1]},together with {0[2]}'.format(position))
    print('{0:_},and {0:_x}'.format(10000000000000000)) #使用下划线作为分隔符？ 此时，0:_x可0:_#x不可


#格式化的字符串常量
def FormatString():
    name='liuao'
    address='CUG 56# 245'
    print(f'my name is {name},and I am living in {address}') # do not forger r in front of '

#字符串的常用方法和操作
#find()、rfind()、index()、rindex()、count()

def commonstroperate1():
    s='dad,mom,grandfather,dad,grandmother,brother,sister,grandson'
    print(s.find('dad'))
    print(s.find('mom'))
    print(s.find('dad',4)) #返回的似乎都是数字，是单词第一次出现的第一个字符的位置
    print(s.rfind('grand')) #可以从后往前查找
    #find和rfind可以用数字指定范围find(str,上限,下限)
    print(s.index('dad')) #返回字符串首次出现的位置，那和find有什么区别呢？


commonstroperate1()