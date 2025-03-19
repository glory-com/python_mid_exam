# 题目F：实现函数max_in_list
# 实现max_in_list函数。输入一个数组，计算数组中所有出现过的整数或者浮点数的最大值；数组中元素若为组合数据类型，只可能是元组、列表或集合；若数组中不包括任何整数和浮点数，则返回None。


#方法一
#将所有的数都拆解出来，在ans列表中包括了所有的整型和浮点数，用max函数求最大值
def max_in_list(data):
    ans = []

    #拆解韩式
    def f(a):
        for i in a :
            #如果是整型或者浮点型，将这个数加入到ans中
            if type(i) == int or type(i) == float :
                ans.append(i) 
            #如果是可迭类型，调用f函数，继续拆解
            if type(i) == set or type(i) == list or type(i) == tuple :
                f(i)

    f(data)
    #如果ans长度为0，说明没有浮点或者整型，返回None
    if len(ans) == 0 :
        return None 
    else :
        return max(ans)
    
#方法二
#直接查找每一个数，不断更新mx
def max_in_list(data):
    #初始化mx为一个很小的值
    mx = -1000
    
    def f(a) :
        #表明mx是函数外的值
        nonlocal mx 
        for i in a :
            #原理同上
            if type(i) == int or type(i) == float :
                mx = max(mx , i)
            if type(i) == set or type(i) == list or type(i) == tuple :
                f(i)
    f(data)
    #如果mx没有改变，说明没有整型或者浮点型
    if mx == -1000 :
        return None 
    return mx 
    
        

