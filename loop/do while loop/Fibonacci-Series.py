a, b = 0, 1
i = 0
while True:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
    if i >= 10:
        break