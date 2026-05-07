shopping = {}

while True:
    print("\n1. Add Item")
    print("2. View Items")
    print("3. Delete Item")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        shopping[item] = price
        print(item, "added successfully!")

    elif choice == "2":
        if shopping == {}:
            print("Shopping list is empty")
        else:
            print("\nShopping List:")
            for item, price in shopping.items():
                print(item, ":", price)

    elif choice == "3":
        item = input("Enter item to delete: ")
        if item in shopping:
            del shopping[item]
            print(item, "deleted successfully!")
        else:
            print("Item not found")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again")