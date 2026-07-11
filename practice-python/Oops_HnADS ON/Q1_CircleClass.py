class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_circumference(self):
        return 2 * 3.14 * self.radius


class Driver:
    def __init__(self):
        c = Circle(5)
        print("Area:", c.get_area())
        print("Circumference:", c.get_circumference())


if __name__ == "__main__":
    Driver()
