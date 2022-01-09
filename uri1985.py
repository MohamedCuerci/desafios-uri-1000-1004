

# mac

numPedidos = int(input(''))

for i in range(1, numPedidos+1):
    codigo, qtde = input('').split()

    qtde = int(qtde)

    total = 0

    if codigo == '1001':
        total += qtde * 1.50
    elif codigo == '1002':
        total += qtde * 2.50
    elif codigo == '1003':
        total += qtde * 3.50
    elif codigo == '1004':
        total += qtde * 4.50
    elif codigo == '1005':
        total += qtde * 5.50

print(f'{total:.2f}')