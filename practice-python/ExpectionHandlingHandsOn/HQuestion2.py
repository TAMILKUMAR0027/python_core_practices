n="5"

try:
    n=int(n)
    print(n*n)
except:
    print("Error: Invalid input.")
finally:
    print("Execution complete")