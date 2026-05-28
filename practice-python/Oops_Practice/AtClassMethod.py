class AtClassMethod:

    pi = 3.14

    def __init__(self, r=1.0, color='red'):
        self.r = r
        self.color = color

    @classmethod
    def getArea(cls, radius):
        return cls.pi * radius * radius

    def __str__(self):
        return f"Circle={self.r}, color={self.color}"


obj = AtClassMethod(1.3)
obj1 = AtClassMethod(2)
obj2 = AtClassMethod(8)

print(
    AtClassMethod.getArea(obj.r),
    AtClassMethod.getArea(obj1.r),
    AtClassMethod.getArea(obj2.r)
)