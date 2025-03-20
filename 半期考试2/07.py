# 题目G：实现函数min_in_list_2
# 实现min_in_list_2函数。输入一个数组，计算数组中所有出现过的整数或者浮点数中第二小的值以及该值对应的索引。数组中元素只可能是整数、浮点数或者字符串；若数组中包括的整数和浮点数的个数小于2，则返回None；若数组中第二小的数出现多次，则返回第一次出现时的索引；若第二小的数和最小的数相等，则顺序在前的为最小的数。

def min_in_list_2(data):
    #记录不是整型和浮点型的数的个数
    cnt = 0
    for idx in range(len(data)):
        #对于不是整型或者浮点型的数，将其转换为100000 一个很大的数
        if not isinstance(data[idx], (int, float)):
            data[idx] = 1000000
            cnt += 1
    #如果整型和浮点型的数量小于两个，返回None
    if len(data) - cnt < 2:
        return None

    #找到第一个最小值的位置
    min_pos = data.index(min(data))
    #将其变为一个很大的值
    data[min_pos] = 10000000
    #找到第二小的数
    ans = min(data)
    pos = data.index(ans)

    return (ans, pos)
