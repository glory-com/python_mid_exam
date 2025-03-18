def dedup_2(dict_a):
    ans = []
    dict = {}
    for i in dict_a :
        if i in dict :
            dict[i] += 1 
        else:
            dict[i] = 1 

        if dict[i] <= 2 :
            ans.append(i)


    return ans 


            
