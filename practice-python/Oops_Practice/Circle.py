class Circle:
    def __init__(self,r=1.0,color='red'):
        self.r=r
        self.color=color
    def getRadius(self):
        return self.r
    def getColor(self):
        return self.color
    def setRadius(self,r):
        self.r=r
    def setColor(self,color):
        self.color=color
    def getArea(self):
        return 3.14*self.r*self.r
    def __str__(self):
        return f"Circle={self.r},color={self.color}"

obj=Circle(1.3)
obj1=Circle(2)
obj2=Circle(3)
print(obj.getArea(),obj1.getArea(),obj2.getArea())
        