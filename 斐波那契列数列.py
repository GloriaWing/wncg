'''
a = 0
b = 1
x = int(input())
while b < x:
    print(b, end=',')
    a, b = b, a + b
'''
'''
#前n项斐波那契列数列
lis = []
n = int(input())
for i in range(n):
    if i == 0 or i == 1:
        lis.append(1)
    else:
        lis.append(lis[i-2]+lis[i-1])

print(lis)        
'''
