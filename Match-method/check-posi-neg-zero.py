num = int(input("Enter number: "))

match num:
    case n if n > 0: print("Positive")
    case n if n < 0: print("Negative")
    case _: print("Zero")