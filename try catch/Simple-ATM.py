balance = 5000

try:
    amount = int(input("Enter withdraw amount : "))

    if amount > balance:
        print("Insufficient balance")
    else:
        print("Withdraw successful")

except ValueError:
    print("Enter valid amount")