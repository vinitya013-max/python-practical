accounts={}
def create_account():
    acc_no = input("enter account number:")
    name = input("enter account holder name:")
    balance = float(input("Enter Initial Balance: "))
    accounts[acc_no] = {"name":name,"balance":balance}
    print("....account created....")

def view_accounts():
    if not accounts:
        print("no account available.")
        return
    for acc_no, details in accounts.items():
        print(f"Account:{acc_no},Name:{details['name']},Balance:{details['balance']}")

def deposit():
    acc_no = input("Enter account number:")
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        print("Deposit successful.")
    else:
        print("Account not found.")

def withdraw():
    acc_no1 = input("Enter account number:")
    if acc_no1 in accounts:
        amount = float(input("Enter amount of withdraw:"))
        if amount <= accounts[acc_no1]["balance"]:
            accounts[acc_no1]["balance"] -= amount
            print("Withdraw Successfully.")
        else:
            print("insuficent fund.")
    else:
        print("account not found.")

def search_account():
    acc_no = input("Enter account number to search:")
     
while True:
    print("\n ---Bank Management---")
    print("1. Created account")
    print("2. View account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Search account")
    print("6. exit")

    choice = input("Enter choice:")
    if choice == '1':
        create_account()
    elif choice == '2':
        view_accounts()
    elif choice == '3':
        deposit()
    elif choice == '4':
        withdraw()
    elif choice == '5':
        search_account()
    elif choice =='6':
        break
    else:
        print("invalid choice:")
