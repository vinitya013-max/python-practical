import numpy as np
r = int(input("enter row: "))
c = int(input("Enter coloum: "))
print(f"Enter {r*c} elements for the array:")
elements = [int(input(f"Element {i+1}: ")) for i in range(r*c)]
arr = np.array(elements).reshape((r,c))

totl = 0
print("Iterating through array: ")
for i, row in enumerate(arr):
    for j, val in enumerate(row):
        print(f"arr[{i},{j}] = {val}")
        total += val

print("Sum of all elements:", total)
