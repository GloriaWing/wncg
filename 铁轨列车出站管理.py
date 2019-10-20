print('案例39：铁轨列车出站管理的运行输出运行结果')
target = {}
C = {}
isOk = 1
top = 0  #top为栈顶
A = 1  #A为进入的车厢的编号
B = 1
n = int(input(""))
targetStr = input("").split(" ")  #输入车厢出站的顺序

for index in range(0, len(targetStr), 1):
    target[index+1] = int(targetStr[index])

while B <= n:
    if A == target[B]:  #判断进站车厢的编号与出站车厢的编号是否相同
        A += 1
        B += 1
    elif (top != 0) and (C[top] == target[B]):  #如果不同，判断栈顶与出站车厢编号是否相同
        top -= 1     #出站（出栈）
        B += 1      #下一个车厢进入
    elif A <= n:     #否则判断车辆是否全部进站
        top += 1
        C[top] = A
        A += 1   #进站（进栈）
    else:
        isOk = 0    #车厢全部进站后仍不符合
        break


if isOk:
    print("YES")
else:
    print("No")
