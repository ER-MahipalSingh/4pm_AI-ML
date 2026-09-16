class Demo:
    def show(self):
        self.name = "Jhon"
        self.age = 20
        print(self.name)
        print(self.age)

obj = Demo()
obj.age = 50
obj.show()


class Students:
    def setData(self, name, age):
        self.name = name
        self.age = age
        
    def getData(self):
        print(self.name, self.age)

stu1 = Students()
stu2 = Students()

stu1.setData("Jhon", 20)
stu1.getData()

stu2.setData("David", 22)
stu2.getData()


class BankAccount:
    def __init__(self, _accBalance):
        self._accBalance = _accBalance
    
    def deposit(self, amount):
        self._accBalance += amount
        print("Amount Deposited")
        print("Total balance ", self._accBalance)
    
    def withdraw(self,amount):
        self._accBalance -= amount
        print("Amount withdraw")
        print("Remaning balance ",self._accBalance)
        
    def __del__(self):
        print("Thanks for visit")
        
acc = BankAccount(5000)

acc.deposit(3000)
acc.withdraw(1000)
    

        