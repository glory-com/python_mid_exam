# E 二进制下1的个数find1
# 二进制下1的个数
# 给定一个自然数a，输出a在二进制表示下1的个数。

def find1(a):
    return list(bin(a)[2:]).count('1')



print(find1(7))