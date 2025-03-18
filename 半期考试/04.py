def sum_int_list(input_list, target):
    ans = []
    for i in range(len(input_list) - 1) :
        for j in range(i + 1, len(input_list)) :
            if input_list[i] + input_list[j] == target :
                ans.append((i,j))

    ans.sort()
    return ans
    
print(sum_int_list([2, 7, 11, 15], 9))