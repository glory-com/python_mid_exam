# B 字符串加密encrypt
# 题目：字符串加密
# 在传输信息的过程中，为了保证信息的安全，我们需要对原信息进行加密处理，形成加密信息，从而使得信息内容不会被监听者窃取。

# 现在输入一个字符串，对其进行加密处理。 加密的规则如下:

# 1.字符串中的小写字母，a加密为b。b加密为 c, ..., y 加密为 z，z 加密为 a。

# 2.字符串中的大写字母，A 加密为 B，B 加密为 C, ...,Y 加密为 Z，Z加密为 A。

# 3.字符串中的其他字符，不作处理。

# 请你输出加密后的字符串



def encrypt(a):
    ans = str()
    for i in  a :
        if ord('a') <= ord(i) <= ord('z') :
            n = (ord(i) - ord('a') + 1 ) % 26  + ord('a')
            res = chr(n) 
            ans += res 

        elif ord('A') <= ord(i) <= ord('Z') :
            n = (ord(i) - ord('A') + 1 ) % 26  + ord('A')
            res = chr(n)
            ans += res 

        else :
            ans += i 


    return ans 


