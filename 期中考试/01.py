# A 实现函数is_prime
# 题目：实现函数is_prime
# 一个大于1的自然数，如果除了1和它自身外，不能被其他自然数整除则称该数为质数。例如 7就是一个质数，因为它只能被1和7整除。 现在，给定一个大于1的自然数，它是质数，输出True，否则输出False


def is_prime(a):
    nums = [True] * (a + 1)
    for num in range(2 , a // 2 + 1) :
        for i in range(2 , a  // num + 1) :
            nums[num * i] = False 

    return nums[-1]


     
