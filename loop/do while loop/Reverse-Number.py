num = 123
rev = 0
while True:
    if num == 0:
        break
    rev = rev * 10 + num % 10
    num //= 10
print("Reverse =", rev)