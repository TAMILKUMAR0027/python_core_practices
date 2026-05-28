class Student2:
    def getStudent(self):
        self.__roll=input("Enter the roll number: ")
        self.__name=input("Enter the name: ")
    def display(self):
        print("Roll number : ",self.__roll,"Name: ",self.__name)
        
class Marks(Student2):
    def getMarks(self):
        self.getStudent()
        self.__m1=float(input("M1: "))
        self.__m2=float(input("M2: "))
        self.__m3=float(input("M3: "))
    def printMark(self):
        self.display()
        print("Mark 1: ",self.__m1)
        print("mark 2: ",self.__m2)
        print("Mark 3: ",self.__m3)
    def calTotal(self):
        return self.__m1+self.__m2+self.__m3
    
class Result(Marks):
    def getResult(self):
        self.getMarks()
        self.__total=self.calTotal()
    def putResult(self):
        self.printMark()
        print("Total marks out 300: ",self.__total)
        
obj=Result()
obj.getResult()
obj.putResult()