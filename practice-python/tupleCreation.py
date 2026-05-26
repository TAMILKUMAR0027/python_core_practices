t = 1, 2, 3, 4, 5
print(t)
print(id(t))
print(t[::-1])
t = (10,) + t[1:]
print(t)
print(id(t))
