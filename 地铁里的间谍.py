print('案例44：地铁里的间谍的输出运行结果')
import numpy as np

has_train = np.zeros((100, 100, 2))
dp = np.zeros((100, 100))
# has_train = [[[0]*2]*100]*100
# dp=[[0]*100]*100
# print(np.array(has_train).shape)
n = int(input())
T = int(input())
t = [0]
t1 = [0] * (100 - n)
t2 = list(map(int, input().split()))
t.extend(t2)
t.extend(t1)
# print(t)
M1 = int(input())
M1a = list(map(int, input().split()))
for i in range(M1):
    i1 = i
    for j in range(1, n + 1):
        has_train[M1a[i]][j][0] = 1
        M1a[i] = M1a[i] + t[j]
M2 = int(input())
M2a = list(map(int, input().split()))

for i in range(M2):
    i1 = i
    for j in range(n, 0, -1):
        has_train[M2a[i]][j][1] = 1
        M2a[i] = M2a[i] + t[j - 1]
for i in range(1, n):
    dp[T][i] = 100
dp[T][n] = 0
for i in range(T - 1, -1, -1):
    for j in range(1, n + 1, 1):
        dp[i][j] = dp[i + 1][j] + 1
        if (j < n and has_train[i][j][0] > 0 and i + t[j] <= T):
            dp[i][j] = min(dp[i][j], dp[i + t[j]][j + 1])
        if (j > 1 and has_train[i][j][1] > 0 and i + t[j - 1] <= T):
            dp[i][j] = min(dp[i][j], dp[i + t[j - 1]][j - 1])
if (dp[0][1] < 100):
    print("所需最少时间为", dp[0][1])
else:
    print("impossible")
