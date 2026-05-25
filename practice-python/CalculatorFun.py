def addition(a, b):
    return a + b


def substraction(a, b):
    return abs(a - b)


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


while True:

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4: Division")
    print("Inputs are not 1,2,3,4 then program is ended")
    Choice = input("Enter the choice: ")
    if Choice == "1":
        a = int(input("Enter num1: "))
        b = int(input("Enter num2: "))
        print(addition(a, b))
    elif Choice == "2":
        a = int(input("Enter num1: "))
        b = int(input("Enter num2: "))
        print(substraction(a, b))
    elif Choice == "3":
        a = int(input("Enter num1: "))
        b = int(input("Enter num2: "))
        print(multiply(a, b))
    elif Choice == "4":
        a = int(input("Enter num1: "))
        b = int(input("Enter num2: "))
        print(division(a, b))
    else:
        break
