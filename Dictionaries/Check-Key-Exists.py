data = {"name": "Vinit", "age": 17}

key = input("Enter key to check: ")

if key in data:
    print("Key exists")
else:
    print("Key not found")