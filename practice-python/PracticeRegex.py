import re

text = "Hi hello everyone ? kgood morning today date is 03 june 2026 ! year"
print(re.findall("\AHi", text))
print(re.findall(r"\byear", text))
print(re.findall("\Bgood", text))
print(re.findall("\D",text))
print(re.findall("\d",text))
print(re.findall("\W",text))
print(re.findall("\w",text))
print(re.findall("\s",text))
print(re.findall("year\Z",text))
