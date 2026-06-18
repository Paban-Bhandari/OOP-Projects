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

    def prescribe(self, patient, medicines):
        prescription = Prescription(self,patient,medicines)
        patient.add_prescription(prescription)
        print(f"Dr. {self.name} prescribed medicines to {patient.name}")
class Nurse(Person):
    def __init__(self, id, name, age,ward):
        super().__init__(id, name, age)
        self.ward=ward

    def display_info(self):
        print("---------- NURSE ----------")
        super().display_info()
        print(f"Ward: {self.ward}")

    def assist(self,appointment):
        print(f"Nurse {self.name} is assisting Dr. {appointment.doctor.name} with patient {appointment.patient.name}")
class Patient(Person):
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self.__appointments = []
        self.__prescriptions=[]
        self.__bills=[]

    @property
    def appointments(self):
        return self.__appointments

    @property
    def prescriptions(self):
        return self.__prescriptions

    @property
    def bills(self):
        return self.__bills

    def display_info(self):
        print("---------- PATIENT ----------")
        super().display_info()

    def add_appointment(self,appointment):
        self.__appointments.append(appointment)

    def add_prescription(self,prescription):
        self.__prescriptions.append(prescription)

    def add_bill(self,bill):
        self.__bills.append(bill)

    def show_record(self):
        print("\n----- PATIENT RECORD -----")
        self.display_info()
        print("\nAppointments:")
        for appointment in self.__appointments:
            print(f"{appointment.reason} | Dr. {appointment.doctor.name} | {appointment.date} | {appointment.status}")
        print("\nPrescriptions:")
        for prescription in self.__prescriptions:
            print(f"Dr. {prescription.doctor.name}")
            for medicine,dosage in prescription.medicines:
                print(f"{medicine} -> {dosage}")
        print("\nBills:")
        for bill in self.__bills:
            print(f"{bill.description} | Rs {bill.amount} | {bill.status}")
class Appointment:
    def __init__(self,doctor,patient,reason,date,time):
        self.doctor=doctor
        self.patient = patient
        self.reason=reason
        self.date=date
        self.time=time
        self.status="Scheduled"

    def complete(self):
        self.status = "Completed"
        print(f"Appointment of {self.patient.name} completed.")

class Prescription:
    def __init__(self,doctor,patient,medicines):
        self.doctor = doctor
        self.patient = patient
        self.medicines = medicines
        

class Bill:
    def __init__(self,patient,description,amount):
        self.patient=patient
        self.description=description
        self.__amount=amount
        self.__status="Unpaid"

    @property
    def amount(self):
        return self.__amount
    
    @property
    def status(self):
        return self.__status
    
    def bill_pay(self):
        self.__status="Paid"
        print("Bill Paid Successfully !!")
    
class Hospital:
    def __init__(self):
        self.doctors=[]
        self.nurses=[]
        self.patients=[]
        self.appointments=[]

    def add_doctor(self,doctor):
        self.doctors.append(doctor)

    def add_nurse(self,nurse):
        self.nurses.append(nurse)

    def add_patient(self,patient):
        self.patients.append(patient)

    def book_appointment(self,doctor,patient,reason,date,time):
        appointment = Appointment(doctor,patient,reason,date,time)
        self.appointments.append(appointment)
        patient.add_appointment(appointment)
        return appointment

    def issue_bill(self,patient,description,amount):
        bill = Bill(patient,description,amount)
        patient.add_bill(bill)
        return bill

    def show_all_appointments(self):
        print("\n----- ALL APPOINTMENTS -----")
        for appointment in self.appointments:
            print(f"Patient : {appointment.patient.name}")
            print(f"Doctor : {appointment.doctor.name}")
            print(f"Reason : {appointment.reason}")
            print(f"Date : {appointment.date}")
            print(f"Time : {appointment.time}")
            print(f"Status : {appointment.status}")
            print("-"*20)