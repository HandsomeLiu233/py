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
        self.master.geometry('577x257')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.Label1Var = StringVar(value='手机：')
        self.Label1Font = Font(font=('宋体',24))
        self.Label1 = Label(self.top, text='手机：', anchor='w', textvariable=self.Label1Var, font=self.Label1Font)
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.042, rely=0.187, relwidth=0.127, relheight=0.16)

        self.Text1Var = StringVar(value='123')
        self.Text1Font = Font(font=('宋体',18))
        self.Text1 = Entry(self.top, text='123', bg='#008000', textvariable=self.Text1Var, font=self.Text1Font)
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.236, rely=0.156, relwidth=0.598, relheight=0.191)
        self.Text1Var.trace('w', self.Text1_Change)

        self.Command1Var = StringVar(value='华为手机')
        self.Command1Font = Font(font=('宋体',12))
        self.Command1 = Button(self.top, text='华为手机', textvariable=self.Command1Var, command=self.Command1_Cmd, font=self.Command1Font)
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.042, rely=0.623, relwidth=0.362, relheight=0.253)

        self.Command2Var = StringVar(value='苹果手机')
        self.Command2Font = Font(font=('宋体',12))
        self.Command2 = Button(self.top, text='苹果手机', textvariable=self.Command2Var, command=self.Command2_Cmd, font=self.Command2Font)
        self.Command2.setText = lambda x: self.Command2Var.set(x)
        self.Command2.text = lambda : self.Command2Var.get()
        self.Command2.place(relx=0.527, rely=0.623, relwidth=0.362, relheight=0.253)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Text1_Change(self, *args):
        #TODO, Please finish the function here!
        pass

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        self.Text1Var = StringVar(value='华为手机')
        self.Text1Font = Font(font=('宋体', 18))
        self.Text1 = Entry(self.top, text='123', bg='#008000', textvariable=self.Text1Var, font=self.Text1Font)
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda: self.Text1Var.get()
        self.Text1.place(relx=0.236, rely=0.156, relwidth=0.598, relheight=0.191)
        self.Text1Var.trace('w', self.Text1_Change)

        pass

    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        self.Text1Var = StringVar(value='苹果手机')
        self.Text1Font = Font(font=('宋体',18))
        self.Text1 = Entry(self.top, text='123', bg='#008000', textvariable=self.Text1Var, font=self.Text1Font)
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.236, rely=0.156, relwidth=0.598, relheight=0.191)
        self.Text1Var.trace('w', self.Text1_Change)
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

