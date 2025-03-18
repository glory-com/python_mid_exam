def is_divisible(a):
    if not isinstance(a , int) :
        return "None" 
    

    a = str(abs(a))
    num = 0 
    for i in a :
        num += int(i)


    a = int(a)



    if a % num == 0 :
        return "Yes"
    
    else :
        return "No"
    



print(is_divisible(10))