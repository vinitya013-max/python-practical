try:
    a = int(input("enter number:"))
    b = int(input("enter number:"))

    print(a/b)

except ZeroDivisionError:
    print("divide by zero error")

except ValueError:
    print("invalid input")