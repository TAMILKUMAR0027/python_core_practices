num=0
def largest(n):
   global num
   if num<n:
       num=n
  

while True:
    n=int(input("Enter the number: "))
    if n!=0:
        largest(n)
    else:
        break
    
print(num)
    