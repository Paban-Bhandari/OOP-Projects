"""
5. School Management System
Person
├── Student
├── Teacher
└── Principal

Features:
Add marks
Generate report card
Assign teachers to classes
Calculate GPA

Concepts:
Inheritance
Polymorphism
Encapsulation
"""

class Person:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

    def display_info(self):
        print(f"\nID : {self.id}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

class Principal(Person):
    def __init__(self,id,name,age):
        super().__init__(id,name,age)

    def display_info(self):
        print("\n------ PRINCIPAL ------")
        super().display_info()

class Teacher(Person):
    def __init__(self,id,name,age,subject):
        super().__init__(id,name,age)
        self.subject = subject
        self.assigned_classes = []

    def assign_class(self,class_name):
        if class_name not in self.assigned_classes:
            self.assigned_classes.append(class_name)

    def show_classes(self):
        print("\nAssigned Classes:")
        for class_name in self.assigned_classes:
            print(class_name)

    def display_info(self):
        super().display_info()
        print(f"Subject : {self.subject}")
        print("Assigned Classes:")
        for class_name in self.assigned_classes:
            print(class_name)

class Student(Person):
    def __init__(self,id,name,age,grade):
        super().__init__(id,name,age)
        self.grade = grade
        self.marks = {}
        self.__gpa = 0

    @property
    def gpa(self):
        return self.__gpa

    def display_info(self):
        super().display_info()
        print(f"Class : {self.grade}")

    def add_marks(self,subject,marks):
        self.marks[subject] = marks

    def calculate_gpa(self):
        if not self.marks:
            return 0
        total = sum(self.marks.values())
        average = total / len(self.marks)
        self.__gpa = round(average / 25, 2)
        return self.__gpa

    def generate_report_card(self):
        print("\n----------- REPORT CARD -----------")
        self.display_info()
        print("\nSubjects:")
        for subject, marks in self.marks.items():
            print(f"{subject} : {marks}")
        print(f"\nGPA : {self.calculate_gpa()}")
        print("------------------------------------")

class School:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self,student):
        self.students.append(student)

    def add_teacher(self,teacher):
        self.teachers.append(teacher)

    def show_students(self):
        print("\n------ STUDENTS ------")
        for student in self.students:
            student.display_info()

    def show_teachers(self):
        print("\n------ TEACHERS ------")
        for teacher in self.teachers:
            teacher.display_info()


# -------------------- TEST --------------------

school = School("Welfare Academy")

principal = Principal(1,"Anita Kayasta",45)
principal.display_info()


t1 = Teacher(101,"Bhabana Bhandari",35,"English")
t1.assign_class(1)
t1.assign_class(2)

t2 = Teacher(102,"Kabita Dhakal",40,"Math")
t2.assign_class(9)
t2.assign_class(10)

school.add_teacher(t1)
school.add_teacher(t2)

school.show_teachers()

t1.show_classes()


s1 = Student(1,"Sima Shrestha",18,10)
s1.add_marks("Math",90)
s1.add_marks("English",85)
s1.add_marks("Science",78)

s2 = Student(2,"Sampada Aacharya",8,2)
s2.add_marks("Math",99)
s2.add_marks("English",100)
s2.add_marks("Science",89)

school.add_student(s1)
school.add_student(s2)

school.show_students()

s1.generate_report_card()
s2.generate_report_card()