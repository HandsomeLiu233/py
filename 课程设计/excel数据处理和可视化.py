

#冒泡排序
def bubble(lst):
    print('遵循我的召唤，开始冒泡排序！')
    length = len(lst)
    for i in range(0, length):
        flag = False
        for j in range(0, length - i - 1):
            #二维数组的冒泡排序
            judge = lst[j][3] < lst[j + 1][3]  # 如果前小于后
            if judge:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # 交换顺序
                flag = True
        if not flag:
            break

#文件操作，读入二维表
txtname='student.txt'
fopen = open(txtname, 'r')
lines = fopen.readlines()
info=[]
for line in lines:
    line=line.strip().split(' ')
    info.append(line)

#文本数字转化为数字
for kk in range(len(info)):
    info[kk][3]=int(info[kk][3])

#冒泡排序
bubble(info)

def luquyiben():
    global yiben
    global yibenman
    print('===========下面是一本录取名单===========')
    for ii in range(len(info)*0.2):
        yiben=yiben+1
        print(info[ii])
        if info[ii][2]=='男':
            yibenman=yibenman+1
    print('===========一本录取名单结束===========')

def luquerben():
    print('===========下面是二本录取名单===========')
    global erben
    global erbenman
    for ii in range(len(info)):
        if info[ii][3]>=440:
            erben=erben+1
            print(info[ii])
            if info[ii][2]=='男':
                erbenman=erbenman+1
    print('===========二本录取名单结束===========')


yiben=0
yibenman=0
erben=0
erbenman=0
luquyiben()
luquerben()



print('一本录取的录取率为',yiben/len(info),'男女比例（男比女)为',yibenman/(yiben-yibenman))
print('二本录取的录取率为',erben/len(info),'男女比例（男比女)为',erbenman/(erben-erbenman))





