# 题目D：实现函数reverse_words
# 实现reverse_words函数，将输入字符串中的每个单词都逆序后返回，注意单词的顺序不能改变，单词之间用空格分隔，字符串中没有标点符号。

def reverse_words(a):
    #使用split函数分词
    a = a.split(' ')
    ans = str()

    for word in a :
        #反转每一个词
        word = word[::-1]
        #加入ans中
        ans += word + ' '
        
    return ans[:-1] #去除ans中最后一个空格
