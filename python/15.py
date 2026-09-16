# class Parent:
#     def show(self):
#         print("Parent class")
        
# class Child(Parent):
#     def aum(self):
#         print("Child class")
        
# obj = Child()
# obj.aum()
# obj.show()


# class A:
#     def show(self):
#         print("Class A")

# class B(A):
#     def show1(self):
#         print("Class B")
        
# class C(B):
#     def show2(self):
#         pass
    
# obj = C()
# obj.show()
# obj.show1()
# obj.show2()

# class A:
#     def show(self):
#         print("Class A")
        
# class B(A):
#     def show1(self):
#         print("Class B")
        
# class C(A):
#     def show2(self):
#         pass
    
# obj = C()
# obj1 = B()
# obj.show2()
# obj.show()

# obj1.show1()

class A:
    def show(self):
        print("Class A")
        
class B():
    def show1(self):
        print("class B")
        
class C(A, B):
    def show2(self):
        print("Class C")
    
class D(B):
    def shoe3(self):
        print("class D")
        
objD = D()

objD.shoe3()

objC= C()

objC.show2()