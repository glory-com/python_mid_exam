# C 实现函数sort_strings
# 题目：实现函数sort_strings
# 实现sort_strings函数。输入是一个字符串列表（由字母和数字组成），按照如下特定规则对其进行排序：对于每个字符串，计算其中包含的数字之和作为权重，按照数字之和由大到小排序，如果没有包含数字则认为权重为0；权重相同时按照字符串原始字典序排列。


def sort_strings(ls):
    def cmp(a) :
        ans = 0 
        for i in a :
            if ord('0') <= ord(i) <= ord('9') :
                ans -= int(i)
        return (ans , a)
    ls = sorted(ls , key = cmp)
    return ls 



sort_strings(["B", "A"])