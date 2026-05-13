try:
    age = int(input("Enter age : "))

    if age < 18:
        raise Exception("Not eligible")

    print("Eligible")

except Exception as e:
    print(e)