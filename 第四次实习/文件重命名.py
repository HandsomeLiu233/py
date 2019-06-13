from os import listdir,rename
from os.path import join,isfile,isdir,splitext
import shutil



def listfile(directory):
    global i
    for subpath in listdir(directory):
        path=join(directory,subpath)
        if isfile(path):
            print(path)
            if subpath.endswith('.jpg'):
                print('发现jpg文件')
                shutil.copy(path,r'U:\test')
                rename(join(r'U:\test',subpath),join(r'U:\test',(str(i)+'.jpg')))
                i=i+1

        elif isdir(path):
            listfile(path)

    print('迁移结束，一共迁移了',i-1,'个jpg文件')



i=1
listfile(r'U:\Users\liuao\Desktop\122')