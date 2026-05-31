a=3
b=4

try:
    if not(type(a) in [int,float] and type(b) in [int,float]):
        raise TypeError
    print(a*b)
except TypeError:
    print("Error: Invalid operand type!")