# 题目A：实现函数sort_odd_and_even
# 实现sort_odd_and_even函数。如果输入不是一个列表或者输入列表的元素不全是整数，返回None； 如果输入列表的元素均为整数，首先将奇数从大到小排序，其后将偶数按照从小到大排序；如果输入为空列表，返回空列表。


def sort_odd_and_even(a):



    #如果a不是一个列表，返回None
    if type(a) != list :
        return None 
    
    #循环检查是否a中有非整数
    for i in a :
        if not isinstance(i,int) :
            return None
    
    else :
        l1 = [] #记录奇数
        l2 = [] #记录偶数

        for i in a :
            if i % 2 == 1 :
                l1.append(i)
            else:
                l2.append(i)

        
        l1.sort(reverse=True)#奇数正排序
        l2.sort(reverse=False)#偶数倒排序
        ans = l1 + l2 

    return ans 

    

