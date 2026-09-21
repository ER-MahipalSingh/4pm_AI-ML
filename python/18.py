# file = open("text.txt", "w")
# file1 = open("text.txt", "r")
# # data = open("text.txt", "r")

# file.write("Hello")
# file.write("\nHello Python")
# # print(data)

# readFile= file1.read()
# print(file1.read())

# file.close()

# a = 10
# b = 0
# c = a / b
# print(c)

# try:
#     a = 10
#     b = 0
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#     print("Can not divisible by 0")
# finally:
#     print("Thanks for calu....")

# try:
#     num = int(input("Enter a number:"))
#     print(num)
# except:
#     print("Invalid number")


accBalance = 5000

try:
    print("Account balance: ", accBalance)
    
    amount = int(input("Enter withdrow amount:"))
    if amount <= 0:
        raise ValueError("Inavlid amount")

    if amount > accBalance:
        raise ValueError("Insufficuent fund")
    
    accBalance -= amount
except ValueError as e:
    print("error: ",e)
else:
    print("Withdrow amount", amount)
    print("Remaning balance", accBalance)
    print("Transaction successfull")
finally:
    print("Thanks for visit")