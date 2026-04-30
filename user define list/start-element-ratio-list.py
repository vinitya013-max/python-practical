thislist = []
n = int(input("Enter number of items: "))

for i in range(n):
    item = input("Enter item: ")
    thislist.append(item) 

start = int(input("Enter starting index: "))

print("Full list:", thislist)
print("After index", start, ":", thislist[start:])