from os import listdir
from  os.path import join,isfile,isdir

def listonlydir(directory):
    for subpath in listdir(directory):
        path=join(directory,subpath)
        if isfile(path):
            print(path)
        elif isdir(path):
            print(path)
            listdir(path)

listonlydir(r"U:\\")
