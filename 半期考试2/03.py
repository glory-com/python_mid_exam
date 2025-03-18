def recursive_digit_sum(a):
    a = str(a) 
    
    while int(a) > 9 :
        ans = 0 
        for i in a :
            ans += int(i)
        a = str(ans)


    return int(a)



print(recursive_digit_sum((678)))