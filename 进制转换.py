x = int(input("请输入一个十进制数："))
n = int(input("请输入一个进制n:"))

def con(x,n):
    result = ''
    if x:
        result = con(x // n, n)
        return result + str(x % n)
    else:
        return result
print(con(x, n))

