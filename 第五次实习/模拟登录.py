def insert():
    global info
    txtname='user.txt'
    fopen = open(txtname, 'r')
    lines = fopen.readlines()
    info=[]
    for line in lines:
        line=line.strip().split(' ')
        info.append(line)

insert()


#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from tkinter import *
from tkinter.font import Font
#Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
from tkinter.messagebox import *
#Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
#import tkinter.filedialog as tkFileDialog
#import tkinter.simpledialog as tkSimpleDialog  #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('408x282')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.Label1Var = StringVar(value='用户名')
        self.Label1Font = Font(font=('宋体',18))
        self.Label1 = Label(self.top, text='用户名', anchor='w', textvariable=self.Label1Var, font=self.Label1Font)
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.039, rely=0.113, relwidth=0.218, relheight=0.145)
        self.Label1.bind('<Button-1>', self.Label1_Button_1)

        self.Label2Var = StringVar(value='密码')
        self.Label2Font = Font(font=('宋体',18))
        self.Label2 = Label(self.top, text='密码', anchor='w', textvariable=self.Label2Var, font=self.Label2Font)
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.039, rely=0.369, relwidth=0.218, relheight=0.145)

        self.Text1Var = StringVar(value='')
        self.Text1Font = Font(font=('宋体',12))
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=self.Text1Font)
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.314, rely=0.113, relwidth=0.551, relheight=0.145)

        self.Text2Var = StringVar(value='')
        self.Text2Font = Font(font=('宋体',12))
        self.Text2 = Entry(self.top, textvariable=self.Text2Var, font=self.Text2Font,show='*')
        self.Text2.setText = lambda x: self.Text2Var.set(x)
        self.Text2.text = lambda : self.Text2Var.get()
        self.Text2.place(relx=0.314, rely=0.369, relwidth=0.551, relheight=0.145)

        self.Command1Var = StringVar(value='登录')
        self.Command1Font = Font(font=('宋体',14,'bold'))
        self.Command1 = Button(self.top, text='登录', textvariable=self.Command1Var, command=self.Command1_Cmd, font=self.Command1Font)
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.51, rely=0.681, relwidth=0.414, relheight=0.23)

        self.Label3Var = StringVar(value='欢迎进入本系统')
        self.Label3Font = Font(font=('宋体',9))
        self.Label3 = Label(self.top, text='欢迎进入本系统', anchor='w', textvariable=self.Label3Var, font=self.Label3Font)
        self.Label3.setText = lambda x: self.Label3Var.set(x)
        self.Label3.text = lambda : self.Label3Var.get()
        self.Label3.place(relx=0.02, rely=0.652, relwidth=0.414, relheight=0.23)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Label1_Button_1(self, event):
        #TODO, Please finish the function here!
        pass

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        name=self.Text1.get()
        password = self.Text2.get()
        flag=0 #检验是否通过
        for i in range(len(info)):
            if name==info[i][0] and password==info[i][1]:
                flag=flag+1
        print(flag)
        if flag==1:
            self.Label3Var = StringVar(value='登录成功')
            self.Label3Font = Font(font=('宋体', 13))
            self.Label3 = Label(self.top, text='登录成功', anchor='w', textvariable=self.Label3Var,
                                font=self.Label3Font)
            self.Label3.setText = lambda x: self.Label3Var.set(x)
            self.Label3.text = lambda: self.Label3Var.get()
            self.Label3.place(relx=0.02, rely=0.652, relwidth=0.414, relheight=0.23)
        else:
            self.Label3Var = StringVar(value='登录失败')
            self.Label3Font = Font(font=('宋体', 17))
            self.Label3 = Label(self.top, text='登录失败', anchor='w', textvariable=self.Label3Var,
                                font=self.Label3Font)
            self.Label3.setText = lambda x: self.Label3Var.set(x)
            self.Label3.text = lambda: self.Label3Var.get()
            self.Label3.place(relx=0.02, rely=0.652, relwidth=0.414, relheight=0.23)
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

