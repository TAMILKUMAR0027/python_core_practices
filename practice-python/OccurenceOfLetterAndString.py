Str = input("Enter the string: ")
total_digit = 0
total_letter = 0
for i in Str:
    if i.isnumeric():
        total_digit += 1
    elif i.isalpha():
        total_letter += 1
    else:
        pass
print(total_digit, total_letter)
