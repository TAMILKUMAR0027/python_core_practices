class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def displayInfo(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def displayCarInfo(self):
        self.displayInfo()
        print(f"Model: {self.model}")


if __name__ == "__main__":
    c = Car("Toyota", 2022, "Corolla")
    c.displayCarInfo()
