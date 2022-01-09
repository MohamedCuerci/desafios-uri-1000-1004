

n = int(input())

maximo = 0
flag = 0
for i in range(n):
    x = int(input())
    if x > maximo and flag == 0:
        maximo = x
        flag += 1
    elif x > maximo and flag >= 1:
        maximo = x
        flag += 1

if flag == 1:
    print('S')
else:
    print('N')