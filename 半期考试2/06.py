def max_in_list(data):
    ans = []

    def f(a):

        for i in a :
            if type(i) == int or type(i) == float :
                ans.append(i) 
            
            if type(i) == set or type(i) == list or type(i) == tuple :
                f(i)

    f(data)
    
    if len(ans) == 0 :
        return None 
    else :
        return max(ans)
        

print(max_in_list([5, {16, 2}]))