# 题目 E：实现函数dedup_2
# 实现dedup_2函数。输入一个整数列表list_a，返回另外一个列表list_b，其中的元素是list_a每个元素只保留前两次出现所得到的，保留的元素相对顺序不变（即将超过两次的出现删去）。


def dedup_2(dict_a):
    #ans记录答案
    ans = []
    #用dict记录出现的次数
    dict = {}


    #遍历每一个a中的元素
    for i in dict_a :
        if i in dict :
            dict[i] += 1 
        else:
            dict[i] = 1 

        #如果还没有记录到两个以上，就加入ans中，保证了顺序不变
        if dict[i] <= 2 :
            ans.append(i)


    return ans 


            
