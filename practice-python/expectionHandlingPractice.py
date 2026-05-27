try:
    a = int(input())
    b = int(input())
    c = a / b
except ZeroDivisionError:
    print("cant divide by zero")
except ValueError:
    print("Give the input as integer")
else:
    print("Executed success")
finally:
    print("Executed always")
