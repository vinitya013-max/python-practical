num = 123
total = 0
while True:
    if num == 0:
        break
    total += num % 10
    num //= 10
print("Sum =", total)