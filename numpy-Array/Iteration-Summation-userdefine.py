import numpy as np 
print("👻✌️🍿💸🍔🧓👍first array input: ")
r1, c1 = map(int, input("👍👍enter number of row or coloum:").split())
print(f"Enter {r1 * c1} elements for the first array:")
elements1 = [int(input(f"Element {i+1}: ")) for i in range(r1 * c1)]
a1 = np.array(elements1).reshape((r1, c1))
print("\n✌️ First Array:")
print(a1)
print("\n👻 Second Array Input (same shape required)")
r2, c2 = map(int, input("Enter number of rows and columns (e.g., 2 3): ").split())
if r1 != r2 and c1 != c2:
    print("😈😈 Warning: Arrays must have compatible shapes to join.")
print(f"Enter {r2 * c2} elements for the second array:")
elements2 = [int(input(f"Element {i+1}: ")) for i in range(r2 * c2)]

a2 = np.array(elements2).reshape((r2, c2))
print("\n✌️ Second Array:")
print(a2)

axis = int(input("\n🍔🍿 Enter axis to join (0 = vertical / row-wise, 1 = horizontal / column-wise): "))

if axis == 0:
    result = np.vstack((a1, a2))
    print("\n🍔 Joined Array (Vertical Stack):")
elif axis == 1:
    result = np.hstack((a1, a2))
    print("\n🧓 Joined Array (Horizontal Stack):")
else:
    print("💸 Invalid axis. Use 0 or 1.")
    exit()

print(result)

