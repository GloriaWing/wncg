a = 1
b = 1
while a <= 9:
    i = 1
    while i <= a:
        b = i * a
        print('%d*%d=%d' % (i, a, b), end=' ')
        i = i+1
    print('')
    a = a + 1
