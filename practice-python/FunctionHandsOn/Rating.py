def TenPercent(num):
    return num * 0.1

def TwentyFive(num):
    return num * 0.25

def ThirtyPercent(num):
    return num * 0.3

n = float(input("Enter the salary: "))
rating = float(input("Enter the rating appraisal: "))
if rating >= 1 and rating <= 4:
    print("The salary hiked is : ", n + TenPercent(n))
elif rating > 4 and rating <= 7:
    print("The salary hiked is : ", n + TwentyFive(n))
elif rating > 7 and rating <= 10:
    print("The salary hiked is : ", n + ThirtyPercent(n))
