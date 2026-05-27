import traceback
import math
try:
    a = int(input())
    if a <= 0:
        raise ValueError("This is a negative error")
except ValueError as e:
     traceback.print_exc()
print("Successfully handled")
print(factorial(5))