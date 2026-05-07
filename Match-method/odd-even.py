num = int(input("Enter number: "))

match num % 2:
    case 0: print("Even")
    case _: print("Odd")