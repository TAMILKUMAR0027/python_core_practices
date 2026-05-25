def prime(n):
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


for i in range(1, 101):
    if prime(i):
        print("Prime : ", i)
    else:
        print("Not prime : ", i)
