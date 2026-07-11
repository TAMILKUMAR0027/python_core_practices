class Triangle:
    def __init__(self, a=3, b=4, c=5):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def calculate_perimeter(self):
        return self.a + self.b + self.c


if __name__ == "__main__":
    t = Triangle()
    print("Area:", t.calculate_area())
    print("Perimeter:", t.calculate_perimeter())
