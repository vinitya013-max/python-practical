positive = 0
negitive = 0
zero = 0
n = int(input("enter ="))
for i in range(1, n+1):
    num = int(input("Enter number= "))
    if num > 0:
        positive += 1
    elif num < 0:
        negitive += 1
    else:
        zero += 1
print("Positive =",positive)
print("Negative =",negitive)
print("Zero =",zero)