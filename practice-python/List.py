t = list()
str = "Tamil"
t = list(str)
print(type(t))
print(t)
for i in range(len(t)):
    print(t[i])
print("----------")
for e in t:
    print(e)
print("----------")
del t[3]
print(t)
del t
print(t)
