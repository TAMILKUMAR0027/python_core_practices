import re
text=r"Hi hello everyone good morning"

res1=re.search("hello",text)
print(res1.group())
print(res1.start())
print(res1.end())
print(res1.span())
print(res1.string)
print(res1.re)
print(