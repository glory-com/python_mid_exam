def string_sorting(string_list):
    n = len(string_list)
    
    #创建一个答案列表，用于等待数值输入
    ans = ["w"] * n 


    for i in range(n) :
        if isinstance(string_list[i],str):
            continue 

        #如果不是字符串，将string_list厘米按的数，放入ans中的相同位置
        #并且将string_list中这个位置的数标记为 mis，用于之后的删除
        else:
            ans[i] = string_list[i]
            string_list[i] = "mis"


    #去除所有的mis，对所有字符串排序
    while "mis" in string_list :
        string_list.remove("mis")


    string_list.sort()

    j = 0
    
    #循环找到所有的非字符串，按原位放回ans中
    for i in string_list :
        while ans[j] != 'w' :
            j += 1 
        else:
            ans[j] = i 
        
            
        
    return(ans)




