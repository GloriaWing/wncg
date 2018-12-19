min = int(input("min:"))
max = int(input("max:"))
sushu = []
for i in range(min,max+1):
    fg = 0
    for j in range(2,i):
        if (i % j) == 0:
            fg = 1
            break
    if (fg == 0):
       sushu.append(i)
print(sushu)
