# 题目E：整数数字逆序
# 实现int_reverse函数。输入一个整数，将整数中的数字逆序，返回逆序后的整数；若输入不是整数，返回None。、

def int_reverse(data):
    #检测输入类型
    if type(data) != int :
        return None 
    #如果是0，直接输出0，防止下面判断正负出错
    if data == 0 :
        return 0 
    
    else :
        flag = abs(data) // data #标记正负号
        data = abs(data)
        data = int(str(int(data))[::-1]) * flag #转换为字符串反转
        return data

