num = 12345
count = 0
while True:
    if num == 0:
        break
    count += 1
    num //= 10
print("Digits =", count)