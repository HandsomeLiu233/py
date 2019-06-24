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
        self.master.geometry('436x336')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.Label1Var = StringVar(value='123')
        self.Label1Font = Font(font=('宋体',9))
        self.Label1 = Label(self.top, text='123', anchor='w', textvariable=self.Label1Var, font=self.Label1Font)
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.073, rely=0.143, relwidth=0.314, relheight=0.17)
        self.Label1.bind('<Button-1>', self.Label1_Button_1)

        self.Text1Var = StringVar(value='')
        self.Text1Font = Font(font=('宋体',9))
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=self.Text1Font)
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.459, rely=0.143, relwidth=0.406, relheight=0.193)

        self.Command1Var = StringVar(value='3333')
        self.Command1Font = Font(font=('宋体',9))
        self.Command1 = Button(self.top, text='3333', textvariable=self.Command1Var, command=self.Command1_Cmd, font=self.Command1Font)
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.679, rely=0.69, relwidth=0.222, relheight=0.217)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Label1_Button_1(self, event):
        #TODO, Please finish the function here!
        pass

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

