s1 = 'abc'
s2 = 'xyz'

res = ""

for i in range(len(s1)):
    res += s1[i]
    res += s2[len(s2)-1-i]

print(res)