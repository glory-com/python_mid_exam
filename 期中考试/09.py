# I 奇怪的字典序2sorted_with_weird_order2
# 题目：奇怪的字典序2sorted_with_weird_order2
# 在英文字典中，排列单词的顺序是先按照第一个字母以升序排列（即a、b、c……z 的顺序）；如果第一个字母一样，那么比较第二个、第三个乃至后面的字母。如果比到最后两个单词不一样长（比如，sigh 和 sight），那么把短者排在前。我们把这种排序方式称为字典序。

# 然而，为什么字母顺序应该是a-z呢？现在有人规定字母顺序应该按照字母在数据中出现的频率从大到小进行排序，若出现频率相同，则按照a-z的顺序进行排序。

# 请实现sorted_with_weird_order2(string_list)函数。将string_list中包含的字符串（字符串中只包含小写字母）按照上述规则定义的字母顺序定义的字典序进行排序。

def sorted_with_weird_order2(string_list):
    dic = {}
    for i in string_list :
        for ch in i :
            if ch in dic :
                dic[ch] += 1 
            else :
                dic[ch] = 1 

    dic = dict(sorted(dic.items() , key = lambda x : (-x[1] , x[0])))
    dic = list(dic.keys())
  
    

    def cmp(a) :
        ans = []
         
        for i in a :
            ans.append(dic.index(i))

        return tuple(ans)
    


    ans = sorted(string_list , key = cmp)

    return ans 




print(sorted_with_weird_order2(['c', 'b', 'a']))
print(sorted_with_weird_order2(['', 'ab', 'b']))
print(sorted_with_weird_order2(['ccc', 'bb', 'a', 'd']))