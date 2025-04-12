# G 去除列表中包含重复字符的字符串remove_dupstr_fromlist
# 题目：去除列表中包含重复字符的字符串remove_dupstr_fromlist
# 实现remove_dupstr_fromlist函数。输入一个列表L，仅去除该列表中包含重复字符的字符串元素。例如列表[123,'121','123']，第2个元素为字符串且包含重复字符'1'，返回列表中应去除该元素：[123,'123']。

def remove_dupstr_fromlist(L):
    ans = []
    for i in L :
        if not isinstance(i , str) :
            ans.append(i)

        else :
            flag = True 
            for ch in i :
                if i.count(ch) > 1 :
                    flag = False 
                    break 

            if flag :
                ans.append(i)


    return ans 



print(remove_dupstr_fromlist([121,'121','123']))
                    

