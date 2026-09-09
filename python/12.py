a = 10

def show():
    print(a)
    b = 20
    print(b)

print(b)

show()
show()
show()
show()

def display(name):
    print(name)

display("Python")

# def sum(a,b):
#     return a + b

# res = sum(10,5)
# print(res)

# def show():
#     return 10, "Java"

# res = show()
# print(res)


# max = lambda a, b: a > b

# print(max(15,10))


# def fact(n):
#     if n == 1: return 1
#     return n * fact(n - 1)

# res = fact(5)
# print(res)


def display():
    """Display fun. is used for value display only"""
    print("Hello")
    
display()
print(display.__doc__)

# def num(*args):
#     print(args)
    
# num(10,20,30,40,5, "python", 20.5)

# def data(**user):
#     print(user)
#     print(type(user))
    
# res = data(name="jhon", age=20)
# print(type(res))

def num(*n):
    for i in n:
        print(i)
        
num(10,20,30)
