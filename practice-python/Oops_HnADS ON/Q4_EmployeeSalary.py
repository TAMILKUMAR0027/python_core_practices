class Employee:
    def getInfo(self, salary, hours_per_day):
        self.salary = salary
        self.hours_per_day = hours_per_day

    def AddSal(self):
        if self.salary < 500:
            self.salary += 10

    def AddWork(self):
        if self.hours_per_day > 6:
            self.salary += 5

    def display_salary(self):
        print("Final Salary:", self.salary)


if __name__ == "__main__":
    emp = Employee()
    emp.getInfo(450, 8)
    emp.AddSal()
    emp.AddWork()
    emp.display_salary()
