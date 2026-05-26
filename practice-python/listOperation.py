a = [1, 23, 5, 50, 6]
a.sort()
b = ["AEF", "GHI", "AjC", "JKL"]
c = sorted(b)
b.sort()
print(b)
print(a)
print(c)
print(c == b)
f = a.copy()
print(f is a)
print(b is c)
