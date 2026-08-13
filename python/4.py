# first = int(input("Enter first value: "))
# second = int(input("Enter second value: "))

# operator = input("Enter operator (+, -, *, /): ")

# match operator:
#     case "+":
#         print("first + second = ", first + second)
    
#     case "-":
#         print("first - second = ", first - second)
        
#     case "*":
#         print("first * second = ", first * second)
        
#     case "/":
#         if second != 0:
#             print("first / second = ", first / second)
#         else:
#             print("not divesiable by 0")
            
#     case _:
#         print("Invalid operator")


# days = int(input("Enter day: "))

# match days:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday's")
    
#     case 6 | 7:
#         print("Weekend")
    
#     case _:
#         print("Invaid day")


accountBalance = 5000

print("-------Welcome-------")
print("1. Balance check")
print("2. Withdraw amount")
print("3. Deposit amount")

choice = int(input("Enter yor choice: "))

match choice:
    case 1:
        print("Account balance is ", accountBalance)
        
    case 2:
        withdrowamount = int(input("Enter withdraw amount: "))
        
        if withdrowamount > accountBalance:
            print("Insufucient balance")
           
        # elif withdrowamount > accountBalance:
        else:
            accountBalance = accountBalance - withdrowamount
            print("Withdraw amount done")
            print("Withdraw amount is ", withdrowamount)
            print("Remainig balance: ", accountBalance)
            
    case 3:
        depositAmount = int(input("Please enter deposit amount: "))
        
        if depositAmount <= 0:
            print("invalid deposit amount")
        else:
            accountBalance = accountBalance + depositAmount
            print("Deposit successfull: ", depositAmount)
            print("Total balance: ", accountBalance)
            
    case _:
        print("Invalid choice")
        