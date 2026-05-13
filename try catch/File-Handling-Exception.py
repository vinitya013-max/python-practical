try:
    f = open("demo.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("file not found")