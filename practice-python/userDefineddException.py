class Error(Exception):
    pass


class ValueTooSmall(Error):
    pass


class ValueTooLarge(Error):
    pass


number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))

        if i_num < number:
            raise ValueTooSmall

        elif i_num > number:
            raise ValueTooLarge

        break

    except ValueTooSmall:
        print("This value is too small, try again!")

    except ValueTooLarge:
        print("This value is too large, try again!")

print("Congratulations! You guessed it correctly.")
