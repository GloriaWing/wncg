x = int(input())
sum = 0
n = len(str(x))
m = x
while m > 0:
    a = m % 10
    sum += a ** n
    m //= 10
if x == sum:
    print(x,"是阿姆斯特朗数")
else:
    print(x,"不是阿姆斯特朗数")
