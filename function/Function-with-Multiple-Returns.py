def calc(a, b):
    return a+b, a-b

x = int(input("enter num="))
y = int(input("enter num="))

x, y = calc(x, y)
print(f"Sum:{x} Difference: {y}")