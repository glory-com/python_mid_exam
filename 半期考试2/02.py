# 题目B：实现密码合法性检查
# 输入一个字符串，检测是否是合法的密码：
# 1）密码必须是一个字符串
# 2）密码必须包含6~12个字符
# 3）密码至少包含一个大写字母、一个小写字母和一个数字
# 4）密码至少包含三个特殊字符"$#@"中的一个
# 返回： 如果是一个合法的密码，返回True，否则返回False


def password_check(a):

    #检查是否是字符串
    if type(a) != str :
        return False 
         
    #检查字符串长度
    if len(a) < 6 or len(a) > 12 :
        return False 
    
    #通过ASCII码，检查是否有一个大写，小写字母，和数字
    flag1 , flag2 , flag3 = False , False , False 
    for i in a :
        if ord("A") <= ord(i) <= ord("Z") :
            flag1 = True 
        if ord("a") <= ord(i) <= ord("z") :
            flag2 = True
        if ord("0") <= ord(i) <= ord('9') :
            flag3 = True


    if not(flag1 and flag2 and flag3) :
        return False 
    
    #检查是否含有特殊字符
    if '$' not in a and  '#' not in a and '@' not in a :
        return False 
    

    return True 


