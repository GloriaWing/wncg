#十进制转化为二，八，十六进制的函数调用
digit = int(input("十进制\n"))
print("二进制为", bin(digit))
print("八进制为", oct(digit))
print("十六进制为", hex(digit))


#二,八，十六进制转换为十进制
digital = input("二进制字符串\n")
print("转为十进制:\n", int(digital, 2))
number = input("八进制的字符串\n")
print("转为十进制:\n", int(number, 8))
figure = input("十六进制的字符串\n")
print("转为十进制:\n", int(figure, 16))
