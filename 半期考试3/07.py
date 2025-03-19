# 题目G：总上升段数
# 一位登山爱好者从起点开始，每隔一段时间记录其海拔高度直至终点。登山结束后，他想知道在登山过程中他的总上升段数，海拔的连续上升计为一段。编写一个函数，帮这位登山爱好者计算总上升高度及上升段数，输入是一个整数列表，数据是按照时间排列的海拔高度记录，输出总上升段数。你可以假设输入的数组中至少有两个数。

def total_ascend(h):
    ans = 0 
    flag = False 

    for i in range(1 , len(h)) :
        if h[i] > h[i - 1] :
            if not flag :
                ans += 1 
                flag = True 
        else :
            flag = False 

    return ans 


h = [100, 200, 150, 250]

total_ascend(h)