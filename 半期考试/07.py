def valid_string(string , dic):
    n = len(string)
    dp = [False] * (n + 1)

    dp[0] = True

    for i in range(1,n+1):
        for j in range(i) :
            if dp[j] and string[j:i] in dic :
                dp[i] = True 


    return (dp[-1])

valid_string("aabbcc",{"a","b","c"})
