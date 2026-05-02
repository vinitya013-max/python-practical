email = "vinityadav123@gmail.com" 
password =1717
counter=0
while counter <3:        
    a = input("enter email id:")
    b = int(input("enter password:"))
    if a == email and b == password:
        print("login successfully")
        break
    else:
        counter+=1
        print("")
if counter == 3:
    print("try again later....")
