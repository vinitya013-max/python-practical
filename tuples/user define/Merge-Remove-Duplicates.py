t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)

merged = t1 + t2

unique = ()

for i in merged:
    if i not in unique:
        unique = unique + (i,)

print("Merged:", merged)
print("Unique:", unique)