def increment(l2):
    l2=[10,20,30,40,50]
    for i in range(0,len(l2)):
        l2[i]+=5
    print("Address: ",id(l2))

list1=[10,20,20,40,50]
print("Address of list1: ",id(list1))
print(list1)

increment(list1)
print(list1)
