# 题目A：实现函数abstract_value
# 实现abstract_value函数。如果输入是整数或者浮点数，返回它的绝对值；如果输入是可以转换成浮点数的字符串，则转换成数字后再返回绝对值；其它情况返回None


def abstract_value(a):
    #isinstance函数可以判断变量的是否属于某个类型，第一个参数是检测对象，第二个参数是元组，其中包括了检测的类型
    if isinstance(a, (int, float)):
        return abs(a)
    
    #检查是否是可以转换为浮点数的字符串
    elif isinstance(a, str):
        try:
            #尝试转换为float类型，如果可以，返回浮点的绝对值
            num = float(a)
            return abs(num)
        #如果类型错误，返回None
        except ValueError:
            return None
    else:
        return None



