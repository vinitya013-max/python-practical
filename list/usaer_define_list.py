n=int(input("Enter list element value="))
l=[]
for i in range(n):
    data=int(input(f"etner value in {i} = "))
    l.append(data)
search=int(input("Etner search value="))
f=1
for i in l:
    if search == i:
        print(f" {search} value in {i}")
        f=0
        l.remove(i)

        break
if f:
    print(f"srach value {search} not found")
print(l)