lst=[1,2,3,4,5,6]

try:
    print(lst[4])
except IndexError:
    print("Error: Index out of range!")