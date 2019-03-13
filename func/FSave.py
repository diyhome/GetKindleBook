import os

def FSave(path,name,content,m):
    path = os.getcwd()+path
    #  print(path)
    f = open(path,name,m)
    f.write(content)
    f.close()

