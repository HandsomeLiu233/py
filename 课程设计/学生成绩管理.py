

def openfile(lst):
    print('正在读入数据')
    txtname = 'score.txt'
    fopen = open(txtname, 'r',encoding='utf-8')
    lines=fopen.readlines()
    for line in lines:
        line=line.strip().split(' ')
        lst.append(line)

def writefile():
    print('正在将数据写入')
    txtname = 'score.txt'
    fopen = open(txtname, 'w',encoding='utf-8')
    for i in range(len(info)):
        for j in range(len(info[i])):
            fopen.write(info[i][j]+' ')
        fopen.write('\n')
    fopen.close()

def inputinfo():
    while True:
        data=input('请输入学生成绩信息\n 数据按照 学号 姓名 英语 高数 Python语言 依次录入 用空格分开\n输入quit退出\n ')
        if data=='quit':
            break
        data=data.strip().split(' ')
        info.append(data)
        writefile()
        print('数据录入成功')

def search():
    while True:
        SearchWord=input('请输入你想要查找的项目及其数值\n 用空格分开 如：姓名 刘傲\n输入其他数值表示退出\n')
        SearchWord=SearchWord.strip().split(' ')
        if SearchWord[0]=='学号':
            Searchco=0
        elif SearchWord[0]=='姓名':
            Searchco=1
        elif SearchWord[0]=='英语':
            Searchco=2
        elif SearchWord[0]=='高数':
            Searchco=3
        elif SearchWord[0]=='Python语言':
            Searchco=4
        else:
            break

        for i in range(len(info)):
            if info[i][Searchco]==SearchWord[1]:
                print(info[i])

def bubble():
    while True:
        SearchWord=input('请输入你想要排序的项目\n输入其他数值表示退出\n')
        SearchWord=SearchWord.strip().split(' ')
        if SearchWord[0]=='学号':
            Searchco=0
        elif SearchWord[0]=='姓名':
            Searchco=1
        elif SearchWord[0]=='英语':
            Searchco=2
        elif SearchWord[0]=='高数':
            Searchco=3
        elif SearchWord[0]=='Python语言':
            Searchco=4
        else:
            break
        for i in range(0, len(info)): #这里的i应该从0开始，纵使第一行不参与排序
            flag = False
            for j in range(1, len(info) - i - 1):  #第一行不参与排序
                judge = int(info[j][Searchco]) < int(info[j + 1][Searchco])  # 如果前小于后
                if judge:
                    info[j], info[j + 1] = info[j + 1], info[j]  # 交换顺序
                    flag = True
            if not flag:
                break

        print('排序以后的数据显示如下')
        for ii in range(len(info)):
            print(info[ii])



'''
openfile(info)
bubble()
writefile()
'''

def main():
    openfile(info)
    while True:
        print('==========欢迎进入学生成绩管理系统================')
        print('请输入数字以操作本系统')
        print('1 学生成绩查看\n2 学生成绩录入\n3 学生成绩查找\n4 学生成绩排序\n输入其他数字存盘退出')
        choice=input('请输入')
        if choice=='1':
            print('数据显示如下')
            for ii in range(len(info)):
                print(info[ii])
            a=input('按下回车键继续')
        elif choice=='2':
            inputinfo()
        elif choice=='3':
            search()
        elif choice=='4':
            bubble()
        else:
            writefile()
            break

info=[]
main()