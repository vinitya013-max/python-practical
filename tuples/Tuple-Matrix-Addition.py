t1 = ((1, 2, 3), (4, 5, 6))
t2 = ((7, 8, 9), (1, 2, 3))

result = ()

for i in range(len(t1)):
    row = ()
    for j in range(len(t1[i])):
        row = row + (t1[i][j] + t2[i][j],)
    result = result + (row,)

print("Result:", result)