import random

def randomname(shu):
    for i in range(0,shu):
        num=random.choice([1,2])
        name=(random.choice(['赵','钱','孙','李','周','吴','郑','王']))
        name=(name+random.choice(['瓜','吊','抽','日','弟','比','草']))
        if num==2:
            name=(name+random.choice(['瓜','皮','刚','屁','干','插','比','水']))
        print(name)

shu=input('请输入你要生成名字的数量')
randomname(int(shu))
