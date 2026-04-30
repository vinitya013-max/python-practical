n = int(input("Enter number of items: "))
mytuple = ()

for i in range(n):
    item = input("Enter item: ")
    mytuple = mytuple + (item,)   

print("User defined tuple:", mytuple)