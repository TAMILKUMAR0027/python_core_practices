s="bcXYZ784*&ˆdef"
upper=0
lower=0
digit=0
nonalpha=0
for i in s:
    if i.isdigit():
        digit+=1
    elif i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    else:
        nonalpha+=1    
print(upper)
print(lower)
print(digit)
print(nonalpha)