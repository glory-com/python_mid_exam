# 题目C：实现函数recursive_digit_sum
# 实现recursive_digit_sum函数，该函数的功能如下，首先计算输入的非负整数的各位数字之和，如果该和大于9，则重复上述过程，即计算和的各位数字之和，直至求出的和是一个一位数为止，并输出最后的结果

def recursive_digit_sum(a):
    #转化为字符串
    a = str(a) 
    
    #当a大于9时，即为两位数时，不断循环
    while int(a) > 9 :
        ans = 0 
        #求各位数上的和
        for i in a :
            ans += int(i)
        #将整型转换为字符串
        a = str(ans)


    return int(a)
