
lista = []
q = 0
while q < 20:
    x = input()
    lista.append(x)
    q += 1

lista = lista[::-1]

contador = 0
for i in lista:
    print(f'N[{contador}] = {i}')
    contador += 1



