class Parent:
    def son(self):
        print("Class Parent")
        
class Child(Parent):
    def son(self):
        super().son()
        print("Child Class")
        
obj = Child()

obj.son()

class Cal:
    def sum(self,a,b,c=0):
        return a + b + c
    
    def sum(self,a,b,c):
        return a+b+c
    
obj = Cal()

print(obj.sum(10,20,0))
print(obj.sum(1,2,3))
print(obj.sum(100,2,3))
print(obj.sum(1,200,3))


# class Additation:
#     def sum(self, *num):
#         total=0
#         for i in num:
#             total += i
#         return total
    
# obj = Additation()

# print(obj.sum(10,20,30))
# print(obj.sum(10,20,30,40))
# print(obj.sum(10,20,30,50,60))
# print(obj.sum(10,20,30,40,50,60))


# class Parent:
#     pass

# class Child(Parent):
#     pass

# print(issubclass(Child, Parent))
# print(issubclass(Parent, Child))