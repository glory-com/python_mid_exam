def password_check(a):
    if type(a) != str :
        return False 
         

    if len(a) < 6 or len(a) > 12 :
        return False 
    

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
    

    if '$' not in a and  '#' not in a and '@' not in a :
        return False 
    

    return True 

print( password_check("123"))
