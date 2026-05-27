obj=open("Tamil.txt",'r')
data=obj.read(10)
print(data)
obj.close()
obj=open("Tamil.txt",'r')
data=obj.readlines()
for l in data:
    word=l.split()
    print(word)
obj.close()

obj=open("Tamil.txt",'r')
data=obj.readlines()
for l in data:
    word=l.splitlines()
    print(word)