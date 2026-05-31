s = "ython is simple"

words = s.split()
small = words[0]

for i in words:
    if len(i) < len(small):
        small = i

print(small)