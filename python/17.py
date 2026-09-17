from abc import ABC, abstractmethod

# class Engine(ABC):
#     @abstractmethod
#     def type(self):
#         pass
        
# class Bike(Engine):
#     def type(self):
#         print("Bike engine type is patrol")
    
# obj = Bike()
     
# obj.type() 

# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#             pass
        
# class CreditCard(Payment):
#     def pay(self,amount):
#         print(f"Payment maid by credit card amount of {amount}")
        
# class NetBanking(Payment):
#     def pay(self,amount):
#         print(f"Paid by net banking {amount}")
        
# cc = CreditCard()
# nb = NetBanking()

# cc.pay(5000)
# nb.pay(50000)
    
    
class Employee(ABC):
    def __init__(self,salary):
        self.salary = salary
        
    @abstractmethod
    def salaryAmount(self):
        pass
    
class PersonA(Employee):
    def salaryAmount(self):
        print(f"Salary givin of ruppes {self.salary}")
        
class PersonB(Employee):
    def salaryAmount(self):
        print(f"Salary givin of ruppes {self.salary}")
        
p1 = PersonA(5000)
p2 = PersonB(10000)

p1.salaryAmount()
p2.salaryAmount()