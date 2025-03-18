# 题目C：简化版ZigZag遍历
# ZigZag遍历指的是对一个矩阵进行之字形遍历，该遍历在图形图像、视频等领域有重要应用。本题考虑一个简化版的ZigZag遍历，即将矩阵切成从右上至左下的切片，并按照示例中的顺序逐个元素输出。编写代码，对输入的矩阵进行遍历，按顺序输出列表；若输入不是矩阵形式（即内层列表长度不一致），输出空列表。


def simplified_zigzag(l):
    ans = [] #记录答案

    #定义比较函数：排序规则，先排行列之和，再排行
    def cmp(a) :
        return(sum(a) , a[0])

    n = len(l[0])

    #检查矩阵是否合法
    for row in l :
        if len(row) != n :
            return []
        
    #存储排序的位置
    pos_list = []
    
    #将所有位置的索引加入到pos_list中
    for i in range(len(l)) :
        for j in range(len(l[0])) :
            pos = [i , j]
            pos_list.append(pos)

    #按照cmp函数排序
    pos_list.sort(key = cmp)

    #输出
    for i in pos_list :
        row , col = i[0] , i[1]        
        ans.append(l[row][col])


    return (ans)



