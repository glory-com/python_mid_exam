# 题目I：实现函数reverse_even_characters
# 实现reverse_even_characters函数，其输入为全为数字与英文字母（不区分大小写）组成的字符串。现在需要对其进行变换，所有奇数位的字符原地不动，所有偶数位的字符进行从前到后的整体的反转。

def reverse_even_characters(string):
    string = list(string)
    li = []
    #找到索引为奇数的字符，放入li中
    for i in range(len(string)):
        if i % 2 == 1 :
            li.append(string[i])
    #反转索引为奇数的字符
    li = li[::-1]
    #放回string中
    for i in range(len(li)):
        string[2 * i + 1] = li[i]
    #返回字符串
    return (''.join(string))

