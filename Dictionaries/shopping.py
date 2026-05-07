shopping = {}

while True:
    print("1: add item:")
    print("2: view item:")
    print("3: delete item:")
    print("4: exit")

    choice = input("enter no:")

    if choice == "1":
        item = input("Enter product name:")
        price = float(input("Enter product price:"))
        shopping[item] = price
        print(item,"....add successfully....")

    elif choice == "2":
        if shopping == {}:
            print("Shopping list is empty")
        else:
            print("\nShopping List:")
            for item, price in shopping.items():
                print(item, ":", price)
    
    elif choice == "3":
        item = input("Enter item to delete:")
        if item in shopping:
            del shopping[item]
            print(item, "deleted successfully")
        else:
            print("item not found: ")

    elif choice == "4":
        print("...Exit program...")
        break
    else:
        print("Invalid choice, try again")
        