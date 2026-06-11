"""
2. Employee Management System
Employee
├── Manager
├── Developer
└── Designer

Each should override:
calculate_salary()

Add:
Bonus
Overtime
Department

Concepts:
Inheritance
Polymorphism
"""

class Employee:
    def __init__(self,name,base_salary,department):
        self.name = name
        self.base_salary = base_salary
        self.department = department

    def show_details(self):
        print(f"\nName: {self.name}")
        print(f"Department: {self.department}")
        print(f"Position: {employee.__class__.__name__}")
        print(f"Salary: Rs.{self.calculate_salary()}")

class Manager(Employee):
    def __init__(self, name, base_salary, department,bonus):
        super().__init__(name, base_salary, department)
        self.bonus = bonus
        
    def calculate_salary(self):
        return self.base_salary+self.bonus

class Developer(Employee):
    def __init__(self, name, base_salary, department, overtime_hours, overtime_rate):
        super().__init__(name, base_salary, department)
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate

    def calculate_salary(self):
        return self.base_salary+(self.overtime_hours*self.overtime_rate)
    
class Designer(Employee):
    def __init__(self, name, base_salary, department,bonus,overtime_hours, overtime_rate):
        super().__init__(name, base_salary, department)
        self.bonus = bonus
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate
    
    def calculate_salary(self):
        return self.base_salary+self.bonus+(self.overtime_hours*self.overtime_rate)
    

manager = Manager("Paban",25000,"IT",5000)
developer = Developer("Hari",17000,"IT",4,2500)
designer = Designer("Govinda",12000,"IT",2000,2,1000)
employees = [manager,developer,designer]
for employee in employees:
    employee.show_details()