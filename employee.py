"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from abc import ABC,abstractmethod
    
class Contract (ABC): 

    @abstractmethod
    def calculate_pay(self):
        pass

class FixedContract(Contract):

    def __init__(self,hourly_wage,hours_worked):
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_pay(self): 
        return self.hourly_wage * self.hours_worked
    
    def __str__(self):
        return f"contract of {self.hours_worked} hours at {self.hourly_wage}/hour"
    
class SalaryContract(Contract):

    def __init__(self,salary):
        self.salary = salary

    def calculate_pay(self):
        return self.salary
    
    def __str__(self):
        return f"monthly salary of {self.salary}"


class Commission(ABC):

    @abstractmethod
    def calculate_commission(self):
        pass

class FixedCommission(Commission):

    def __init__(self,commission):
        self.commission = commission

    def calculate_commission(self):
        return self.commission
    
    def __str__(self):
        return f"bonus commission of {self.commission}"
    
class VaryCommission(Commission):

    def __init__(self,contracts_landed,commission_per_contract):
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def calculate_commission(self):
        return self.contracts_landed * self.commission_per_contract
    
    def __str__(self):
        return f"commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract"

class Employee:
    def __init__(self, name, contract:Contract,commission:Commission = None):
        self.contract = contract
        self.name = name
        self.commission = commission

    def get_pay(self):
        return self.get_commission()+self.get_contract_pay()

    def get_commission(self):
        return self.commission.calculate_commission() if self.commission else 0
            
    def get_contract_pay(self):
        return self.contract.calculate_pay()

    def __str__(self):
        commission_info = f" and receives a {str(self.commission)}" if self.commission else ""
        return f"{self.name} works on a {str(self.contract)}{commission_info}. Their total pay is {self.get_pay()}."
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',SalaryContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',FixedContract(25,100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',SalaryContract(3000),VaryCommission(4,200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',FixedContract(25,150),VaryCommission(3,220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',SalaryContract(2000),FixedCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',FixedContract(30,120),FixedCommission(600))
