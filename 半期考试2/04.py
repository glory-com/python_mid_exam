def reverse_words(a):
    a = a.split(' ')
    ans = str()
    for word in a :
        word = word[::-1]
        ans += word + ' '
        
    return ans[:-1]


print(reverse_words('python package'))
