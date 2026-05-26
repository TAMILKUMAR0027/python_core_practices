n = int(input("Enter the no of element: "))
lis = []
for i in range(0, n):
    print(f"Enter the element {i+1}")
    lis.append(int(input()))
print(lis)


list1 = input().split(",")
print(type(list1))

list2 = list(map(int, input().split(",")))
print(list2)
