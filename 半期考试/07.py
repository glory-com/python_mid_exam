# 题目G：判断字符串是否由字典中的词组成
# 实现valid_string(string, dictionary)函数。判断字符串string是否由dictionary中的词组合而成，注意同一个词可以在string中出现多次。


def valid_string(string , dic):
    n = len(string)

    #dp[i]表示从开始到字符串中第i个字符能否被字典中的数组成
    dp = [False] * (n + 1)

    #dp[0]表示空字符串，一定能被字典组成
    dp[0] = True

    #枚举结束的位置为i
    for i in range(1,n+1):
        #开始的位置为j
        for j in range(i) :
            #状态转移方程：dp[i] = dp[j] and string[j:i] in dic 
            #如果string[:j]可以被字典表示，并且string[j:i]在字典里面，那么string[:i]就可以被字典表示
            if dp[j] and string[j:i] in dic :
                dp[i] = True 


    return (dp[-1])



def valid_string(string , dic):
    memory = {} #记忆化数组，没有的话会tle
    def dfs(n) :

        #如果已经记录过了，就直接返回
        if n in memory.keys():
            return memory[n]
        
        #当n = len(string)时，截取的为空字符串，返回True
        if n == len(string) :
            return True
        

        else :
            #枚举结束位置
            for i in range(n + 1 , len(string) + 1) :
                #原理同上
                if dfs(i) and string[n:i] in dic :
                    memory[n] = True
                    return True

        memory[n] = False 
        return False
        

    return dfs(0)






