# 题目C：实现函数count_sum_int_float

# 实现sum_int_float函数。 将输入列表中的整数或者浮点数求和，并舍弃其它类型的数据，返回(N, sum)，其中N为列表中数字的个数，sum为它们的和 如list为空或者其中没有整数或者浮点数，返回(0, None)


def count_sum_int_float(input_list):
    ans = 0  #用ans记录和
    count = 0 #用count记录整数或者浮点数的数量

    #枚举每一个数
    for num in input_list :
        #如果是整型或者浮点型，加入ans，并且count+1
        if isinstance(num,(int,float)):
            ans += num 
            count += 1 
    #count=0时，说明list中没有整型或者浮点型，返回None
    if count == 0 :
        return (0 , None)

    else:
        return (count , ans)

