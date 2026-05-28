class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def show(self):
        print("Details : ",self.name,self.color,self.price)
    def max_speed(self):
        print("Vehicle max speed is 150")
    def change_gear(self):
        print("Vehicle change gear 6 ")

class car(Vehicle):
    def max_speed(self):
         super().max_speed()
         print("Car max speed is 240")
    def change_gear(self):
         super().change_gear()
         print("Change gear to 7")

c1=car("Benz",'REd',200000)
c1.show()
c1.max_speed()
c1.change_gear()
v1=Vehicle("Truck","White",12000)
v1.show()
v1.max_speed()
v1.change_gear()