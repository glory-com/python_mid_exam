def word_cut(string, dictionary):
    n = len(string)
    dict = {0: []}

    dp = [0] * (n + 1)
    dp[0] = 0

    check = [False] * (n + 1)
    check[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if check[j] and string[j:i] in dictionary:
                check[i] = True

                if dp[j] + dictionary[string[j:i]] > dp[i]:
                    dp[i] = dp[j] + dictionary[string[j:i]]
                    dict[i] = dict[j] + [string[j:i]]

    if not check[-1] :
        return (None , 0)
    else :
        return (dict[n] , dp[-1])

print(word_cut("南京市长江大桥", {"南京": 10, "南京市": 12, "市长": 10, "长江": 10, "大桥": 10, "长江大桥": 25, "江大桥": 1})
)
