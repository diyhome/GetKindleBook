class Chater():
    def __init__(self):
        print("进入字符串处理...")
    def onchinese(self,text):
        te = ""
        for i in text:
            if i >= u'\u4e00' and i <= u'\u9fa5':
                te = te+i        
        return te

#    def spse(self,text,bnum,dnum):
#        #  使用list[k:] or list[:k]使数组左，右移，覆盖前面特点行
#        tetmp = text.split()
#        print(tetmp)
#        if bnum != "":
#            temp =  tetmp[bnum:]
#        if dnum != "":
#            tetmp = tetmp[:dnum]

