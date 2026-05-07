username = input("Enter username: ")
password = input("Enter password: ")

match (username, password):
    case ("admin", "1234"):
        print("Login Successful")
    case _:
        print("Login Failed")
        