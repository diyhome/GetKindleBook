"""判断一个字符是否为汉字，是则返回True """

def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def only_chinese(text):
    rt=""
    for i in text:
        if is_chinese(i):
            rt = rt+i
    return rt
if __name__ == "__main__":
    u_input = input("Please enter you want:")
    print(only_chinese(u_input))
