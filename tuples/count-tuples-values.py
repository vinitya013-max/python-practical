t =(1,2,2,3,3,3,3,4,4,4,4,4,4)
checked = ()
for i in t:
    if i not in checked:
        count = 0
        for j in t:
            if i == j:
                count += 1
        print(i,"->",count)
        checked = checked + (i,)