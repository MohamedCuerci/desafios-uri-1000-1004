

x, y = input().split()

x = int(x)
y = int(y)

maior = 0

if x == y:
    maior = x
else:
    if x > y:
        maior = x
    else:
        maior = y

print(maior)


