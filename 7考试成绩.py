from random import randint



#可以调用，完美

def score(lst1):
    print('student score function is called')
    for dd in range(100):
        lst1.append(randint(1,100))
    print(lst1)



# 冒泡排序，部分借鉴了书本
def bubble(lst):
    print('遵循我的召唤，开始冒泡排序！')
    length = len(lst)
    for i in range(0, length):
        flag = False
        for j in range(0, length - i - 1):
            judge = lst[j] < lst[j + 1]  # 如果前小于后
            if judge:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # 交换顺序
                flag = True
        if not flag:
            break

def grade(lst):
    print('遵循我的召唤，给成绩分级！')
    convert=[]
    length=len(lst)
    for k in range(0,length):
        if lst[k]<60:
            convert.append(str(lst[k])+'分 不及格')
        elif lst[k]<=69:
            convert.append(str(lst[k])+'分 及格')
        elif lst[k]<=79:
            convert.append(str(lst[k])+'分 一般')
        elif lst[k]<=89:
            convert.append(str(lst[k])+'分 良好')
        else:
            convert.append(str(lst[k])+'分 优秀')
    print(convert)

def convertnew(xx):
    if xx < 60:
        return('分 不及格')
    elif xx <= 69:
        return('分 及格')
    elif xx <= 79:
        return('分 一般')
    elif xx <= 89:
        return('分 良好')
    elif xx<=100:
        return('分 优秀')
    else:
        return('数据不合法喵')


#lst3: List[Union[int, Any]] = [randint(1, 100) for eee in range(100)] #生成随机成绩
#bubble(lst3) #排序
#print(lst3)
#grade(lst3)

#lst1=[]
#score(lst1)
#bubble(lst1)
#grade(lst1)


lst1=[]
score(lst1)

for ii in range(len(lst1)):
   lst1[ii]=(convertnew(lst1[ii]))
print(lst1)