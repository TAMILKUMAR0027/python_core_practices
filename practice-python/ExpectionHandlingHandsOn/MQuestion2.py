class InputNotANumberException(Exception):
    pass

class DivisionByZeroException(Exception):
    pass

class InvalidMultiplierException(Exception):
    pass

op="+"
a=10
b=5

try:
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise InputNotANumberException

    if op=="+":
        print(a+b)

    elif op=="-":
        print(a-b)

    elif op=="*":
        if a in [0,1] or b in [0,1]:
            raise InvalidMultiplierException
        print(a*b)

    elif op=="/":
        if b==0:
            raise DivisionByZeroException
        print(a/b)

except InputNotANumberException:
    print("Invalid Input")
except DivisionByZeroException:
    print("Error: Division by zero is not allowed.")
except InvalidMultiplierException:
    print("Invalid Multiplier")