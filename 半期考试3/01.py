# 题目A：实现函数find_letter
# 实现find_letter函数，其输入为全为小写字母或者数字的字符串。请找出第一个只出现一次的字符，并返回索引，如果这样的字符不存在返回None。

def find_letter(a):

    #记录每一个字符出现的个数
    dict = {}
    for i in a :
        if i in dict :
            dict[i] += 1 
        else :
            dict[i] = 1 

    #取一个很大的数字
    pos = 10000
    

    for key , value in dict.items() :
        if value == 1 :
            #更新最小的位置
            pos = min(pos , a.index(key))

    #如果pos没有变化，说明没有值出现一次的字符
    if pos == 10000 :
        return None

    else :
        return (pos , str(a[pos]))
        
