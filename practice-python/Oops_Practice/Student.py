class Student:
    def __init__(self):
        self._name="Tamil"
        self.__age=39
    def getAge(self):
        return self.__age
class Subject(Student):
    pass

objSub=Subject()
obj=Student()
print(obj._name,obj.getAge())
print(objSub._name,objSub.getAge())