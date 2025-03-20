
# 题目H：实现分词函数word_cut
# 实现word_cut(string, dictionary)函数。将字符串string分割为若干个dictionary中包含的词。

# 注意同一个字符串可能有不同的分词方式，我们需要选择其中最优的一种。因此，dictionary为一个字典，该字典的键为合法的词，对应的值为该词的得分(一个正整数）。一种分词方式的得分即为所有词的得分的和，最优的分词方式为得分和最大的分词方式。

# word_cut函数需要返回一个包含最优分词结果(list)和最优分词结果的得分的元组。若输入为空字符串，应返回([], 0);若字符串不能被分割为字典中的词，应返回(None, 0)。


def word_cut(string, dictionary):
    n = len(string) #string长度
    dict = {0: []} #用dict数组记录到达每一分数的分词方式

    dp = [0] * (n + 1 )#dp[i]表示到达第i个字符的最大值
    dp[0] = 0 #0个字符的最大值为0

    #用check数组记录前i个字符能否有dictionary中组成
    check = [False] * (n + 1)
    check[0] = True


    for i in range(1, n + 1):
        for j in range(i):
            if check[j] and string[j:i] in dictionary:
                check[i] = True #检查是否能够组成

                if dp[j] + dictionary[string[j:i]] > dp[i]:
                    dp[i] = dp[j] + dictionary[string[j:i]] #记录分数
                    dict[i] = dict[j] + [string[j:i]] #不断记录每一个分数的组合

    if not check[-1] : #判断是否能够组成
        return (None , 0)
    else :
        return (dict[n] , dp[-1])

