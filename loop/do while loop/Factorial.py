num = 5
i = 1
fact = 1
while True:
    fact *= i
    i += 1
    if i > num:
        break
print("Factorial =", fact)