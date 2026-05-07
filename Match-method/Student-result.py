m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
m3 = int(input("Enter marks3: "))

total = m1 + m2 + m3
per = total / 3

match per:
    case p if p >= 75: print("Distinction")
    case p if p >= 60: print("First Class")
    case p if p >= 50: print("Second Class")
    case _: print("Fail")