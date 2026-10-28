class Student:
    def __init__(self, name, standard, marks):
        self.name = name
        self.standard = standard
        self.marks = marks

    def category(self):
        if self.marks >= 90:
            return "A grade"
        elif self.marks >= 75:
            return "B grade"
        elif self.marks >= 60:
            return "C grade"
        else:
            return "F grade"

    def display(self):
        print("Name:", self.name)
        print("Standard:", self.standard)
        print("Marks:", self.marks)
        print("Grade:", self.category())


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            student.display()


school = School()

s1 = Student("Aditya", 8, 90)
s2 = Student("Rahul", 9, 80)
s3 = Student("Amit", 10, 30)

school.add_student(s1)
school.add_student(s2)
school.add_student(s3)

school.display_students()