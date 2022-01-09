

while True:
    x, y = input().split()

    resultado = int(x) + int(y) 

    if x == '0' and y == '0':
        break

    valor = int(str(resultado).replace('0', ''))
    print(valor)