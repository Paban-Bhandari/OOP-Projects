"""
6. Hospital Management System
Person
├── Doctor
├── Nurse
└── Patient

Features:
Appointment booking
Patient records
Prescriptions
Billing

Concepts:
Object interaction
Composition
Encapsulation
"""

class Person:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"NAME: {self.name}")
        print(f"Age: {self.age}")
class Doctor(Person):
    def __init__(self, id, name, age,specialization):
        super().__init__(id, name, age)
        self.specialization=specialization
        
    def display_info(self):
        print("---------- DOCTOR ----------")
        super().display_info()
        print(f"Specialization: {self.specialization}")

    def prescribe(self):
        pass
class Nurse(Person):
    def __init__(self, id, name, age,ward):
        super().__init__(id, name, age)
        self.ward=ward

    def display_info(self):
        print("---------- NURSE ----------")
        super().display_info()
        print(f"Ward: {self.ward}")

    def assist(self):
        pass
class Patient(Person):
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self.__appointments = []
        self.__prescriptions=[]
        self.__bills=[]

    def display_info(self):
        print("---------- PATIENT ----------")
        super().display_info()

    def add_appointment(self,appointment):
        self.__appointments.append(appointment)

    def add_prescription(self,prescription):
        self.__prescriptions.append(prescription)

    def add_bill(self,bill):
        self.__bills.append(bill)
class Appointment:
    def __init__(self,doctor,patient,reason,date,time,status):
        self.doctor=doctor
        self.patient = patient
        self.reason=reason
        self.date=date
        self.time=time
        self.status=status

class Prescription:
    def __init__(self,doctor,patient,medicines):
        self.doctot = doctor
        self.patient = patient
        self.medicine = []
        

class Bill:
    def __init__(self,patient,description,amount,status):
        self.patient=patient
        self.description=description
        self.__amount=amount
        self.__status=status

    @property
    def amount(self):
        return self.__amount
    
    @property
    def status(self):
        return self.__status
    
