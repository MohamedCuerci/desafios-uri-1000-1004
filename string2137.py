

while True:
    try:
        n = int(input())
        lista = []
        for i in range(n):
            codigo = int(input())
            lista.append(codigo)

        for y in lista:
            print(f'{y:04}')


    except:
        break