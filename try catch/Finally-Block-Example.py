try:
    a = int(input("enter number:"))
    print(a)

except ValueError:
    print("invalid input")

finally:
    print("program finished")