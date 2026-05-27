obj = open("Dummy.txt", "w")
while True:
    data = input()
    if data=="":
        break
    obj.write(data+"\n")
obj.close()
obj = open("Dummy.txt", "r")
for l in obj:
    print(l)
obj.close()
