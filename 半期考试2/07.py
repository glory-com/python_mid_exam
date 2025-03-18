def min_in_list_2(data):
    cnt = 0
    for idx in range(len(data)):
        if not isinstance(data[idx], (int, float)):
            data[idx] = 1000000
            cnt += 1

    if len(data) - cnt < 2:
        return None

    min_pos = data.index(min(data))
    data[min_pos] = 10000000

    ans = min(data)
    pos = data.index(ans)

    return (ans, pos)




print(min_in_list_2(['a','b','c']))