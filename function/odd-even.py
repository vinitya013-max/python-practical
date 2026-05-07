def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
num = int(input("enter number="))

print(check(num))