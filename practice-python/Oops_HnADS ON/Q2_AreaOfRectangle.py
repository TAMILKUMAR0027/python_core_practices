class Area:
    def setDim(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        return self.length * self.breadth


if __name__ == "__main__":
    obj = Area()
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    obj.setDim(length, breadth)
    print("Area:", obj.getArea())
