#十进制到进制的转换
'''
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
'''
x = int(input("请输入一个十进制数："))
n = int(input("请输入一个进制n:"))

def f(x ,n):
    a = []
    b = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    while True:
        s = x // n #商
        r = x % n #余数
        a.append(r)
        if s == 0:
            break
        x = s
    a.reverse()
    for i in a:
        print(b[i],end='')

f(x,n)
