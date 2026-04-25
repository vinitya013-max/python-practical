num = 121
temp = num
rev = 0
while True:
    if num == 0:
        break
    rev = rev * 10 + num % 10
    num //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")