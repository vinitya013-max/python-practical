student = {}

n = int(input("Enter number of subjects: "))

for i in range(n):
    sub = input("Enter subject: ")
    marks = int(input("Enter marks: "))
    student[sub] = marks

print("Student Marks:", student)