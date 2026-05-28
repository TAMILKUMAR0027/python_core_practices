class Student1:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def getAge(self):
        return self.__age
    def set_age(self,age):
        self.__age=age
    
stud=Student1("Tamil",14)
print("Name: ",stud.name)
print("Age: ",stud.getAge())