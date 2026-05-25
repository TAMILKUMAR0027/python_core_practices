def circle(radius):
    return 3.14 * radius * radius


def rectangle(length, width):
    return length * width


def square(side):
    return side * side


while True:

    print("\n1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Square")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        radius = float(input("Enter radius: "))
        print("Area of Circle =", circle(radius))

    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area of Rectangle =", rectangle(length, width))

    elif choice == "3":
        side = float(input("Enter side: "))
        print("Area of Square =", square(side))

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")