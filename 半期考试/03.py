def count_sum_int_float(input_list):
    ans = 0 
    count = 0 
    for num in input_list :
        if isinstance(num,(int,float)):
            ans += num 
            count += 1 

    if count == 0 :
        return (0 , None)

    else:
        return (count , ans)

