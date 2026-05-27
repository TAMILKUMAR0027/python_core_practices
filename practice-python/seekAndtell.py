f = open("Dummy.txt", "r")

print(f.tell())   

f.read(5)

print(f.tell())   

f.close()