class School:
    totalStudents = 0
    MAX_CAPACITY = 500

    @classmethod
    def enrollStudent(cls):
        if cls.totalStudents < cls.MAX_CAPACITY:
            cls.totalStudents += 1
            print("Student enrolled")
        else:
            print("School is full")

    @classmethod
    def getTotalStudents(cls):
        return cls.totalStudents


if __name__ == "__main__":
    for _ in range(3):
        School.enrollStudent()
    print("Total Students:", School.getTotalStudents())
