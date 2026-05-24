num = int(input("Enter a number: "))

if num % 2 != 0:
    num = (3 * num) + 1
else:
    num = num // 2

print(num)
