str1 = '/*Jon is  @developer & musician!!' 
for i in str1:
    if i.isalnum():
        print(i,end="")
    elif i.isspace():
        print(i,end="")
    else:
        print("#",end="")