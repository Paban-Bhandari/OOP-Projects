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
        print(f"""\nID : {self.id}\nName : {self.name}\nAge : {self.age}""")
class Student(Person):
    def __init__(self, id, name, age,grade):
        super().__init__(id, name, age)
        self.grade=grade
        self.marks={}
        self.gpa=0

    def add_marks(self,subject,marks):
        self.marks[subject]=marks
        
    def calculate_gpa(self):
        if not self.marks:
            return 0
        else:
            total=0
            for key,value in self.marks.items():
                total+=int(value)
            average = total/len(self.marks)
            self.gpa = average/25
            return self.gpa

    def generate_report_card(self):
        print("\n----------- REPORT CARD -----------")
        super().display_info()
        print(f"Grade   : {self.grade}\n")
        print("Subjects:\n")
        for subject, marks in self.marks.items():
            print(f"{subject} : {marks}")
        print(f"\nGPA : {round(self.calculate_gpa(), 2)}\n")
        print("------------------------------------")
        
class Teacher(Person):
    def __init__(self, id, name, age,subject):
        super().__init__(id, name, age)
        self.subject = subject
        self.assigned_classes = []

    def assign_class(self,class_name):
        if class_name not in self.assigned_classes:
            self.assigned_classes.append(class_name)

    def show_classes(self):
        print(f"Teacher: {self.name}")
        print(f"Subject: {self.subject}")
        print("\nAssigned Classes:")
        for class_name in self.assigned_classes:
            print(class_name)

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")
        print("Assigned Classes:")
        for class_name in self.assigned_classes:
            print(class_name)

class School:
    

# s1 = Student(1,"Paban",22,8)

# s1.add_marks("Math", 90)
# s1.add_marks("English", 85)
# s1.add_marks("Science", 78)

# s1.generate_report_card()

# t1 = Teacher(1,"Hari",45,"English")

# t1.assign_class(8)
# t1.assign_class(10)

# t1.show_classes()

# t1.display_info()

