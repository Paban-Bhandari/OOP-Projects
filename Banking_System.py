"""
3. Banking System
Account
├── SavingsAccount
├── CurrentAccount
└── FixedDepositAccount

Features:
Deposit
Withdraw
Interest calculation
Minimum balance checking

Concepts:
Encapsulation
Abstraction
Method overriding
"""
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,acc_holder,balance):
        self.acc_holder = acc_holder
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} deposited successfully")
        print(f"Total Balance: {self.balance}")

    def withdraw(self,amount):
        if self.balance<amount:
            print("Insufficent Balance")
        else:
            self.balance-=amount
            print(f"{amount} withdrawn successfully")
        print(f"Current Balance: {self.balance}")

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingAccount(Account):
    MIN_BALANCE = 1000
    def __init__(self, acc_holder, balance,interest_rate):
        super().__init__(acc_holder, balance)
        self.interest_rate=interest_rate
    
    def calculate_interest(self):
        print(f"Previous Balance = {self.balance}")
        interest = self.balance*(self.interest_rate/100)
        self.balance+=interest
        print(f"""
Interest = {interest}
Current Balance = {self.balance}
""")

    def withdraw(self, amount):
        if self.balance - amount < self.MIN_BALANCE:
            print("Minimum balance must be maintained.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")
            print(f"Current Balance: {self.balance}")


class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 5000

    def __init__(self, acc_holder, balance):
        super().__init__(acc_holder, balance)

    def calculate_interest(self):
        return 0

    def withdraw(self, amount):
        if self.balance + self.OVERDRAFT_LIMIT >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Overdraft limit exceeded")

class FixedDepositAccount(Account):
    def __init__(self, acc_holder, balance,interest_rate):
        super().__init__(acc_holder, balance)
        self.interest_rate=interest_rate

    def calculate_interest(self):
        print(f"Previous Balance = {self.balance}")
        interest = self.balance*(self.interest_rate/100)
        self.balance+=interest
        print(f"""
Interest = {interest}
Current Balance = {self.balance}
""")

    def withdraw(self, amount):
        print("Withdrawal not allowed before maturity.")

sa1 = SavingAccount("Paban",10000,3)
sa1.calculate_interest()
sa1.deposit(200)
sa1.withdraw(4000)

ca1 = CurrentAccount("Parwat",2000)
ca1.calculate_interest()
ca1.deposit(200)
ca1.withdraw(7200)
ca1.withdraw(200)

fa1 = FixedDepositAccount("Tina",1000,8)
fa1.calculate_interest()
fa1.deposit(200)
fa1.withdraw(500)