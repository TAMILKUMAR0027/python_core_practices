from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculateSalary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculateSalary(self):
        return self.salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculateSalary(self):
        return self.hourly_rate * self.hours


class ContractEmployee(Employee):
    def __init__(self, name, contract_amount):
        super().__init__(name)
        self.contract_amount = contract_amount

    def calculateSalary(self):
        return self.contract_amount


if __name__ == "__main__":
    emp1 = FullTimeEmployee("John", 5000)
    emp2 = PartTimeEmployee("Alice", 20, 40)
    emp3 = ContractEmployee("Bob", 3000)

    print(emp1.name, emp1.calculateSalary())
    print(emp2.name, emp2.calculateSalary())
    print(emp3.name, emp3.calculateSalary())
