Greet = "Good day"
print(Greet*3)
a = 10
print(Greet[-6:])
print(Greet[3:3])
print(Greet[-3:-1])
print(Greet[-3:-7])
print(Greet[1:])
print(Greet[::-1])
print(Greet[1:2:1])
print(Greet[:-1:2])
print(Greet[::-2])
str=Greet[::-1]

print(str)
print("---------------")

print(a, Greet, len(Greet))
for i in range(0, len(Greet)):
    print(Greet[i])
print("---------------")
for i in Greet:
    print(i)
