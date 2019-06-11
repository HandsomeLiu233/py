import tkinter
import tkinter.messagebox
import os
import os.path

# path = os.getenv('tmp')
# filename = os.path.join(path, 'info.txt')

root = tkinter.Tk()

root['height'] = 400
root['width'] = 1000


button1=tkinter.Button(root,text='fuck')
button1.place(x=30,y=100,width=60,height=30)


root.mainloop()
