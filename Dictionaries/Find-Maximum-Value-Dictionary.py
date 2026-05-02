marks = {"math": 80, "science": 90, "english": 75}

max_sub = max(marks, key=marks.get)

print("Highest marks in:", max_sub)