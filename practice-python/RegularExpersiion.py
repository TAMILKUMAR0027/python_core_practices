import re
text="Hi hello everyone good morning"

res=re.search("^Hi.*morning$",text)
res2=re.search("^Hi.*everyone.*morning$",text)
print(type(res))
if(res):
    print("yes 1")
else:
    print("no")
if(res2):
    print("yes 2")
print(res)
print(res,res.span())