#杨辉三角
r = int(input())
x = [0] * r
for i in range(0, r):
    for j in range(0, i + 1):
        if j == 0:
            x[0] = x[i] = 1
        elif j > 0 and j < i:
            x[i - j] = x[i - j] + x[i - j - 1]
    k = 0
    x.append(0)
    while x[k] != 0 and k < r:
        print(x[k], end=' ')
        k = k + 1
    print("")
