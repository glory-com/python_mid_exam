# 题目B：实现函数num_dates
# 实现num_dates函数，其输入一个整数型列表，每一个数字表示每一天的日气温，按照日期从小到大排列；输出为从对应的日期算起，多少天后气温才会升高；如果之后都不会升高，对应位置天数为0；如果输入为空列表或者列表中有数值不为整数，则返回None



def num_dates(a):
    #判断输入是否是列表
    if not isinstance(a, list):
        return None
    #检查列表长度是否为0
    if len(a) == 0:
        return None
    #检查列表中是否含有浮点数
    for temp in a:
        if not isinstance(temp, int):
            return None

    ans = []
    
    for pos, temp in enumerate(a):
        #用flag记录后面是否有比它大的数
        flag = True
        #循环后面每一个数
        for i in range(pos + 1, len(a)):
            if a[i] > temp:
                ans.append(i - pos)
                flag = False
                break
        #如果没有比它大的数，添加0
        if flag:
            ans.append(0)

    return ans

