# H 重复数字增长求和sum_digit
# 题目：重复数字增长求和sum_digit
# 实现sum_digit函数，输入两个数a和N，N为非负整数。如果输入的a不是整数，返回0；若a不小于0，则计算s=a+aa+aaa+...+aa...a，共N项求和；如果a小于0，对a取绝对值，计算N项的和后返回其负数：s=-（|a|+|a||a|+...+|a||a|...|a|）。

def sum_digit(a, N):
    if not isinstance(a , int) :
        return 0 
    return sum([int(str(abs(a)) * i) for i in range(1 , N + 1)]) if a > 0 else -sum([int(str(abs(a)) * i) for i in range(1 , N + 1)])
    

print(sum_digit(-12, 2))