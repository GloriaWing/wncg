import random
list = []
for i in range(65, 91):
    a = str(chr(i))
    list.append(a)
for i in range(97, 123):
    a = str(chr(i))
    list.append(a)
for i in range(1, 10):
    list.append(str(i))

def x():
    s = " "
    for i in range(7):
        x = random.choice(list)
        s = s + x
    print(s)

for i in range(1,201):
    x()
