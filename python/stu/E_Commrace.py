while True:
    
    item=int(input("Enter Your Item: "))
    
    match item:
        case 1:
            print("Add To Cart: ")
            
        case 2:
            print("Clear Cart: ")
            
        case 3:
            print("Exit: ")
            
        case _:
            print("Wrong Item Exit")
            break
        