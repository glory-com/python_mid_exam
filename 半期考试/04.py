# 题目D：实现函数sum_int_list
# 实现sum_int_list函数。 该函数第一个参数为一个整数的列表input_list, 第二个参数为一个整数目标值target。 给定整数的列表input_list和一个整数目标值target，如果列表中两个元素之和等于这个整数，则将这两个元素的索引形成一个元组。

# 请按从小到大的顺序输出所有满足条件的元组形成的列表。（提示：可直接使用.sort()方法进行排序）。


def sum_int_list(input_list, target):
    ans = [] #用ans列表存储答案

    #枚举第一个数的索引
    for i in range(len(input_list) - 1) :
        #枚举第二个数的索引
        for j in range(i + 1, len(input_list)) :
            #两数和是否等于target ， 如果是，则添加到ans中
            if input_list[i] + input_list[j] == target :
                ans.append((i,j))

    #从大到小排序
    ans.sort()
    return ans
    
