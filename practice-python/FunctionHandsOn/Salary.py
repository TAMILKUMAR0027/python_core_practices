def Hike(a, b):
    SalaryHike = 0
    SalaryHike = a + (a * (b / 100))
    return SalaryHike


Salary = float(input("Ente the salary: "))
hike = float(input("Enter the hike percentage: "))
print("The salary of the person: ", Hike(Salary, hike))
