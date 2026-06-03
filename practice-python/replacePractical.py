import re
text="Hi hello everyone good morning good "

res=re.sub("good","bad",text)
print(res)
print(type(res))