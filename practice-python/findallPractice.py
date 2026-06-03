import re
text="hi hello everyone good morning good hi"
res=re.findall("good|hi",text)
print(type(res))
if(res):
    print(res)
else:
    print("no")
print(res)

