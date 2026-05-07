shopping = []
def additem(shopping):
    item = input("Enter item name: ")
    shopping.append(item)
    print(item, "added successfully!")


def viewitems(shopping):
    if len(shopping) == 0:
        print("Shopping list is empty")
    else:
        print("\nShopping List:")
        for i in range(len(shopping)):
            print(i + 1, ".", shopping[i])


def deleteitem(shopping):
    item = input("Enter item to delete: ")
    if item in shopping:
        shopping.remove(item)
        print(item, "deleted successfully!")
    else:
        print("Item not found")


def main():

    while True
        print("1. add item")
        print("2. view items")
        print("3. delete item")
        print("4. exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            additem(shopping)
        elif choice == "2":
            viewitems(shopping)
        elif choice == "3":
            deleteitem(shopping)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again")

main()