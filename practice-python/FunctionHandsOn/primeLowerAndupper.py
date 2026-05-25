def prime(n):
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input("Enter the lower bound: "))
m = int(input("Enter the upper bound: "))
if n < m:
    for i in range(n, m + 1):
        if prime(i):
            print("Prime : ", (i))
        else:
            print("Not prime : ", (i))

else:
    print("Provide some valid inputs")
