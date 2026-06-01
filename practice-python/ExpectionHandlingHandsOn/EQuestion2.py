n=5

try:
    n=int(n)
    if n<=0:
        raise ValueError
    print(n)
except ValueError:
    print("Error: Invalid input! Please enter a positive integer.")