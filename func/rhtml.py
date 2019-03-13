import os

def save_file(file_path,file_name,content,modle):
    f=open(file_path,modle)
    f.write(content)
    f.close()
