# 题目 B：实现中位数函数
# 中位数是指将N个数字按照大小排列起来居于数据列表中间位置的数值。当N为偶数时，取中间两个数的平均值， 当N为奇数时，取中间那个数
# 实现list_median函数，输入为含有N个数字的列表，返回它的中位数，如果列表为空则返回None



def list_median(input_list):
    if len(input_list) == 0:
        return None

    input_list.sort()

    if len(input_list) % 2 == 1:
        pos = len(input_list) // 2
        return input_list[pos]
    else:
        pos1 = len(input_list) // 2
        pos2 = pos1 - 1
        return (input_list[pos1] + input_list[pos2]) / 2

