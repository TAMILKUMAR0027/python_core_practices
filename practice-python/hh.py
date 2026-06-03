import re
p=r"\b\w+ing"
text="walking and talking are important activities"
m=re.findall(p,text)
if m:
    print(m)

m1=re.search(p,text)
if m1:
    print(m1.group())