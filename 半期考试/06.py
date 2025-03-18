def string_sorting(string_list):
    n = len(string_list)
    

    ans = ["w"] * n 
    for i in range(n) :

        if isinstance(string_list[i],str):
            continue 
        else:
            ans[i] = string_list[i]
            string_list[i] = "mis"



    while "mis" in string_list :
        string_list.remove("mis")


    string_list.sort()

    j = 0

    for i in string_list :
        while ans[j] != 'w' :
            j += 1 
        else:
            ans[j] = i 
        
            
        
    return(ans)


            
