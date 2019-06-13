import random


# 这个类定义参考来源https://www.cnblogs.com/vaster/p/9874984.html
class Student():
    # 构造函数
    # 对当前对象的实例的初始化
    def __init__(self, name, number, score):
        self.name = name
        self.number = number
        self.score = score

    #   isinstance函数判断一个对象是否是一个已知的类型，类似type
    def get_name(self):
        if isinstance(self.name, str):
            return self.name

    def get_number(self):
        if isinstance(self.number, int):
            return self.number

    def get_score(self):
        a = self.score
        return a

    def classgenerateinfo():
        print('遵循我的召唤，作为类的函数，开始给学生创造成绩')
        for j in range(100):
            z[j] = Student(randomname(), randomnumber(), randomscore())

    def classprintInfo():
        print('作为类的函数，显现吧，学生的成绩')
        for k in range(100):
            print(z[k].get_name(), z[k].get_number(), z[k].get_score())
    def classprintInfo1(self):
        print('作为类2342的函数，显现吧，学生的成绩')
        print(self.get_name(), self.get_number(), self.get_score())



# 随机名字的生成
def randomname():
    for i in range(0, 1):
        num = random.choice([1, 2])
        name = (random.choice(['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '刘', '胡', '江', '彭', '占', '董', '何', '马', '魏']))
        name = (name + random.choice(['瓜', '吊', '抽', '日', '弟', '比', '草', '狗', '飞', '浪', '呆', '臭', '对', '鸡', '鸭']))
        if num == 2:
            name = (name + random.choice(['瓜', '皮', '刚', '屁', '干', '插', '比', '水', '鸟', '蛋', '丑', '头']))
        return (name)


# 随机成绩的生成
def randomscore():
    sss = random.randint(1, 100)
    return (sss)


# 随机学号的生成
def randomnumber():
    nnn = random.randint(100000, 999999)
    return (nnn)


# 建立一个包含100个项目的列表，方便之后把信息放进去。实际上应该用append加入列表，这么做太傻了
z = [0 for i in range(100)]

shu = 100  # 我忘了这个是干啥的了


# 学生信息的生成
def generateinfo():
    print('遵循我的召唤，开始给学生创造成绩')
    for j in range(100):
        z[j] = Student(randomname(), randomnumber(), randomscore())


# 学生成绩的打印
def printInfo():
    print('显现吧，学生的成绩')
    for k in range(100):
        print(z[k].get_name(), z[k].get_number(), z[k].get_score())


# 冒泡排序
def bubble():
    print('遵循我的召唤，开始冒泡排序！')
    length = 100
    for i in range(0, length):
        flag = False
        for j in range(0, length - i - 1):
            judge = z[j].get_score() < z[j + 1].get_score()  # 如果前小于后
            if judge:
                z[j], z[j + 1] = z[j + 1], z[j]  # 交换顺序
                flag = True
        if not flag:
            break


# 成绩转换
def convert(xx):
    # print('遵循我的召唤，转换成绩！')
    if xx < 60:
        return ('不及格')
    elif xx <= 69:
        return ('及格')
    elif xx <= 79:
        return ('一般')
    elif xx <= 89:
        return ('良好')
    elif xx <= 100:
        return ('优秀')
    else:
        return ('数据不合法喵')


Student.classgenerateinfo()
bubble()

# 遍历以转换成绩
for kk in range(100):
    z[kk].score = convert(z[kk].score)

#for x in range(100):
 #   print(z[x].classprintInfo1())

Student.classprintInfo()








print(z[2].name) #由于name是一个公有的对象，可以直接被调用，不需要用get_name调用了，但是调用方法注意，是变量名.成员名