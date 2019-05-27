from random import randint


from typing import List, Any, Union

# 学生成绩生成,这个鬼鬼函数似乎还是不对，函数以外还是无法调用
def score():
    print('student score function is called')
    lst1=[]
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


lst3: List[Union[int, Any]] = [randint(1, 100) for eee in range(100)] #生成随机成绩
bubble(lst3) #排序
print(lst3)
grade(lst3)
