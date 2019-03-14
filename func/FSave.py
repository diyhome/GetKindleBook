import os

def FSave(path,name,content,m):
    path = os.getcwd()+path
    #  print(path)
    if content is not None:
        with open(path+name,m) as f:
            f.write(content)
    else:
        print("Faild in write:")
        print(content)

