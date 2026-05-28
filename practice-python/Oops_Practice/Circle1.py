class Circle1:
    def __init__(self, *args):
        if len(args) == 0:
            self.__radius = 1.0
            self.__color = "red"
        elif len(args) == 1:
            self.__radius = args[0]
            self.__color = "red"
        elif len(args) == 2:
            self.__radius = args[0]
            self.__color = args[1]
        else:
            raise ValueError("Too many arguments")

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def setRadius(self, radius):
        self.__radius = radius

    def setColor(self, color):
        self.__color = color

    def getArea(self):
        return 3.14 * self.__radius * self.__radius

    def __str__(self):
        return f"Circle(radius={self.__radius}, color={self.__color})"


obj1 = Circle1()
obj2 = Circle1(2.5)
obj3 = Circle1(4, "blue")
print(obj1)
print(obj2)
print(obj3)
print("Area of obj1:", obj1.getArea())
print("Area of obj2:", obj2.getArea())
print("Area of obj3:", obj3.getArea())
obj1.setRadius(5)
obj1.setColor("green")
print("Updated obj1:", obj1)
