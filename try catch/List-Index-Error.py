try:
    list1 = [10, 20, 30]

    index = int(input("Enter index : "))

    print(list1[index])

except IndexError:
    print("Index out of range")