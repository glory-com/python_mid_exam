# 题目D：逐项相乘
# 逐项相乘是一个二元运算，其输入（函数参数）为两个相同形状的列表，输出（函数返回值）是具有同样形状的、各个位置的元素等于两个输入列表相同位置元素的乘积的列表。注意，列表可以嵌套，所以输入可以是一维的列表，也可以是二维嵌套列表（矩阵），甚至更高维嵌套的列表。
# 测试样例保证x，y的形状相同，且嵌套列表中保存的数据均为整数。


def elementwise_product(x, y):
    #递归计算
    if isinstance(x, list) and isinstance(y, list):
        return [elementwise_product(a, b) for a, b in zip(x, y)]
    else:
        return x * y
        
x, y = [1], [2]
print(elementwise_product(x, y))






        
