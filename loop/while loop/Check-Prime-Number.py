num = 7
i = 2
flag = True

while i < num:
    if num % i == 0:
        flag = False
        break
    i += 1

if flag:
    print("Prime")
else:
    print("Not Prime")