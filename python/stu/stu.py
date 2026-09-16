while True:
    print("Welcome to Resturant \n")
    
    print("1. View Menu")
    print("2. Confirm Order")
    print("3. Cancel Order")
    print("4. Exit \n")
    choice = int(input("Enter your choice"))
    
    match choice:
        case 1:
            print("-------MENU----------")
            print("Momos")
            print("Maggie")
            print("Samosa")
            print("Tea\n")
            
        case 2:
            print("Your order has been confirmed successfully! Thank You!\n")

        case 3:
            print("Your order has been cancelled!\n")
            
        case 4:
            print("Thank You Visit Again\n")
            break
            
        case _:
            print("Invalid Choice! Try Again\n")
        

    

            
        
            
            
            
    
    