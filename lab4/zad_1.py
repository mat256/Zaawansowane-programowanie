class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Student {self.name}'

    def is_passed(self):
        return self.marks > 50


student1 = Student("Jan", 67)
student2= Student("Michał", 44)

print(student2, student2.is_passed())
print(student1, student1.is_passed())
