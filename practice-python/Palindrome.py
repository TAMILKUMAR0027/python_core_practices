n = input("Enter the string: ")
n2 = input("Enter the string: ")
m = n[::-1]
if n2 == m:
    print("Palindrome")
else:
    print("Not a palindrome")
print(n.__eq__((n2)))