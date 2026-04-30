t = (1, 2, 3, 2, 1)
print(t)
if t == t[::-1]:
    print("Palindrome tuple")
else:
    print("Not palindrome")