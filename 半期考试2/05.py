# 题目E：实现函数is_divisible
# 实现is_divisible函数。如果输入是一个整数，检查该整数能否被其所有数字之和整除（假设输入不会是0

def is_divisible(a):
    #如果a不是int类型，输出None
    if not isinstance(a , int) :
        return "None" 
    
    #将a转换为字符串格式，准备遍历每一个数，并且取绝对值，防止负数影响
    a = str(abs(a))
    num = 0 
    for i in a :
        num += int(i)

    a = int(a)

    #如果能够整除返回yes
    if a % num == 0 :
        return "Yes"
    
    else :
        return "No"
    