students = ()

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students = students + ((name, marks),)

print("\nStudent Records:")
for s in students:
    print(s)

topper = students[0]

for s in students:
    if s[1] > topper[1]:
        topper = s

print("Topper:", topper)