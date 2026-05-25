total=0
def calculateOfOdd(n):
    total=0
    for i in range(1,n+1):
       if i%2!=0:
           total+=i
    return total
def calculateOfEven(n):
    total=0
    for i in range(1,n+1):
        if i%2==0:
            total+=i
    return total
    
n=int(input("Enter the number: "))
print("The odd number sum: ",calculateOfOdd(n))
print("The Even number sum: ",calculateOfEven(n))
