from Interest import Interest

a = int(input("Enter principal amount : "))
b = int(input("Enter rate : "))
c = int(input("Enter time : "))

i = Interest()

print("Interest =", i.simple_interest(a, b, c))