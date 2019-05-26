from random import randint

#学生成绩生成
def score():
    lst1=[randint(1,100) for i in range(100)]
    print(lst1)

#冒泡排序，部分借鉴了书本
def bubble(lst):
    length=len(lst)
    for i in range(0,length):
        flag=False
        for j in range(0,length-i-1):
            judge=lst[j]<lst[j+1] #如果前小于后
            if judge:
                lst[j],lst[j+1]=lst[j+1],lst[j] #交换
                flag=True
        if not flag:
            break

score()
lst1=[randint(1,100) for i in range(100)]
bubble(lst1)
print(lst1)