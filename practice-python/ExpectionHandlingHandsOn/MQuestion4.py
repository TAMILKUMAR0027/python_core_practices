n=666

try:
    n=int(n)
    if str(n)==str(n)[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
except:
    print("Enter only integer numbers")