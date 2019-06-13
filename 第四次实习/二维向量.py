import math

class vector:

    #类的定义
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy

#加
    def plus(self,v2):
        self.x=self.x+v2.x
        self.y=self.y+v2.y
        print('向量相加')
        print(self.x,self.y)

#数乘
    def multiple(self,vv):
        self.x=self.x*vv
        self.y=self.y*vv
        print('向量数乘')
        print(self.x,self.y)

#减
    def cut(self,v3):
        self.x=self.x-v3.x
        self.y=self.y-v3.y
        print('向量相减')
        print(self.x,self.y)

#模
    def mo(self):
        moo=(self.x)*(self.x)+(self.y)*(self.y)
        moo=math.sqrt(moo)
        print('向量的模')
        print(moo)


#定义向量
aa=vector(1,2)
bb=vector(3,4)

#进行实现
aa.plus(bb)  #self这个参数不需要写进去，谁.plus，self就是谁，实质上这个代码等于plus(aa,bb)
aa.multiple(3)
aa.cut(bb)
aa.mo()











