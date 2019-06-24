def insert():
    global info
    txtname='trans.txt'
    fopen = open(txtname, 'r',encoding='utf-8')
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
        self.master.geometry('500x305')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.Label1Var = StringVar(value='查询')
        self.Label1Font = Font(font=('宋体',15))
        self.Label1 = Label(self.top, text='查询', anchor='w', textvariable=self.Label1Var, font=self.Label1Font)
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.016, rely=0.079, relwidth=0.194, relheight=0.161)
        self.Label1.bind('<Button-1>', self.Label1_Button_1)

        self.Text1Var = StringVar(value='')
        self.Text1Font = Font(font=('宋体',9))
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=self.Text1Font)
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.256, rely=0.052, relwidth=0.61, relheight=0.213)

        self.Label2Var = StringVar(value='翻译')
        self.Label2Font = Font(font=('宋体',14))
        self.Label2 = Label(self.top, text='翻译', anchor='w', textvariable=self.Label2Var, font=self.Label2Font)
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.016, rely=0.341, relwidth=0.21, relheight=0.292)

        self.Text2Var = StringVar(value='')
        self.Text2Font = Font(font=('宋体',9))
        self.Text2 = Entry(self.top, textvariable=self.Text2Var, font=self.Text2Font)
        self.Text2.setText = lambda x: self.Text2Var.set(x)
        self.Text2.text = lambda : self.Text2Var.get()
        self.Text2.place(relx=0.256, rely=0.315, relwidth=0.61, relheight=0.633)

        self.Command1Var = StringVar(value='翻译')
        self.Command1Font = Font(font=('宋体',9))
        self.Command1 = Button(self.top, text='翻译', textvariable=self.Command1Var, command=self.Command1_Cmd, font=self.Command1Font)
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.896, rely=0.341, relwidth=0.082, relheight=0.449)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Label1_Button_1(self, event):

        pass

    def Command1_Cmd(self, event=None):
        word=self.Text1.get()
        print(word)
        for i in range(len(info)):
            if word==info[i][0]:
                print(info[i][1])
                self.Text2Var = StringVar(value=info[i][1])
                self.Text2Font = Font(font=('宋体', 9))
                self.Text2 = Entry(self.top, textvariable=self.Text2Var, font=self.Text2Font)
                self.Text2.setText = lambda x: self.Text2Var.set(x)
                self.Text2.text = lambda: self.Text2Var.get()
                self.Text2.place(relx=0.256, rely=0.315, relwidth=0.61, relheight=0.633)
            else:
                self.Text2Var = StringVar(value='找不到这个单词')
                self.Text2Font = Font(font=('宋体', 15))
                self.Text2 = Entry(self.top, textvariable=self.Text2Var, font=self.Text2Font)
                self.Text2.setText = lambda x: self.Text2Var.set(x)
                self.Text2.text = lambda: self.Text2Var.get()
                self.Text2.place(relx=0.256, rely=0.315, relwidth=0.61, relheight=0.633)


        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

