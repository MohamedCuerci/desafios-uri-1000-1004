


n = input()

contagemImpar = 0

for i in n:
    if i == '1':
        contagemImpar += 1


if contagemImpar % 2 != 0:
    print(n+'1')
else:
    print(n+'0')