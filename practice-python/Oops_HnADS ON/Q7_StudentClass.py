class Student:
    def __init__(self, student_id=0, name="", age=0, grade=""):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade


if __name__ == "__main__":
    s1 = Student()
    s2 = Student(101, "Alice", 20, "A")
    print("Default Student:", s1.student_id, s1.name, s1.age, s1.grade)
    print("Parameterized Student:", s2.student_id, s2.name, s2.age, s2.grade)
