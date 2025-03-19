# 题目H：实现函数count_characters
# 实现count_characters函数，其输入为全为英文字母（不区分大小写）的字符串。请按照字母顺序，输出每个出现的字母（以小写形式）以及对应的出现频率，不同字母的信息以“逗号+空格”隔开（行尾不需要打印空格）。

def count_characters(string):
    #转换为小写
    string = string.lower()
    dict = {}
    ans = str()
    #记录次数
    for i in string :
        dict[i] = dict.get(i , 0) + 1 
    #按键排序
    dict = sorted(dict.items())
    #按照格式输出
    for i in range(len(dict)) :
        ans += f"{dict[i][0]}:{dict[i][1]}" if i == len(dict) - 1 else  f"{dict[i][0]}:{dict[i][1]}, "

    return ans 

print(count_characters("zzAAAbb"))