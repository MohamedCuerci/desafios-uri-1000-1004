x, y = input().split()

x = int(x)
y = int(y)

totalAbas = x

for i in range(y):
    acao = input()
    if acao == 'fechou':
        totalAbas += 1
    else:
        totalAbas-=1

print(totalAbas)



