# D 实现函数find_common_strings
# 题目：实现函数find_common_strings
# 实现find_common_strings函数。输入是两个列表（不考虑内部嵌套组合数据类型的情况，但其中的元素可能不全是字符串），找到两个列表中共同的字符串，并且按照字典序排列，返回排序过后的字符串列表。

def find_common_strings(la, lb):
    return sorted([i for i in list(set(la) & set(lb)) if isinstance(i , str)])



print( find_common_strings(["A", "B"],["A1", "B1"]))