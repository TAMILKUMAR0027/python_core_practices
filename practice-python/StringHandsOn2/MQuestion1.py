t1 = ('Manjeet', 'Nikhil', 'Akshat')
t2 = (' Singh', ' Meherwal', ' Garg')

result = tuple(a + b for a, b in zip(t1, t2))

print(result)