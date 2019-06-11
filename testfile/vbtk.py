#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
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
        self.master.geometry('495x293')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.标题Var = StringVar(value='模拟登录')
        self.style.configure('T标题.TLabel', anchor='w', font=('宋体',22))
        self.标题 = Label(self.top, text='模拟登录', textvariable=self.标题Var, style='T标题.TLabel')
        self.标题.setText = lambda x: self.标题Var.set(x)
        self.标题.text = lambda : self.标题Var.get()
        self.标题.place(relx=0.307, rely=0.055, relwidth=0.293, relheight=0.14)
        self.标题.bind('<Button-1>', self.标题_Button_1)

        self.Label1Var = StringVar(value='用户名')
        self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',12))
        self.Label1 = Label(self.top, text='用户名', textvariable=self.Label1Var, style='TLabel1.TLabel')
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.048, rely=0.218, relwidth=0.131, relheight=0.058)
        self.Label1.bind('<Button-1>', self.Label1_Button_1)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.242, rely=0.191, relwidth=0.438, relheight=0.085)

        self.Label2Var = StringVar(value='密码')
        self.style.configure('TLabel2.TLabel', anchor='w', font=('宋体',12))
        self.Label2 = Label(self.top, text='密码', textvariable=self.Label2Var, style='TLabel2.TLabel')
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.048, rely=0.355, relwidth=0.131, relheight=0.085)

        self.Text2Var = StringVar(value='Text2')
        self.Text2 = Entry(self.top, textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.setText = lambda x: self.Text2Var.set(x)
        self.Text2.text = lambda : self.Text2Var.get()
        self.Text2.place(relx=0.242, rely=0.355, relwidth=0.438, relheight=0.085)

        self.Command1Var = StringVar(value='登录')
        self.style.configure('TCommand1.TButton', font=('宋体',15,'bold'))
        self.Command1 = Button(self.top, text='登录', textvariable=self.Command1Var, command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.129, rely=0.628, relwidth=0.487, relheight=0.167)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def 标题_Button_1(self, event):
        #TODO, Please finish the function here!
        pass

    def Label1_Button_1(self, event):
        #TODO, Please finish the function here!
        pass

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

