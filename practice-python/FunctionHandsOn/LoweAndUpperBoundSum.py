total=0
def calculateOfOdd(n,m):
    total=0
    for i in range(n,m+1):
       if i%2!=0:
           total+=i
    return total
def calculateOfEven(n,m):
    total=0
    for i in range(n,n+1):
        if i%2==0:
            total+=i
    return total
lowerBound=int(input("Enter the lower bound: "))
upperbound=int(input("Enter the upper number: "))
print("The odd number sum: ",calculateOfOdd(lowerBound,upperbound))
print("The Even number sum: ",calculateOfEven(lowerBound,upperbound))
