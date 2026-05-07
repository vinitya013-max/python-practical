marks = int(input("Enter marks: "))

match marks:
    case m if m >= 90: print("A")
    case m if m >= 75: print("B")
    case m if m >= 50: print("C")
    case _: print("Fail")