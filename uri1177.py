


n = int(input())

contador = 0

for i in range(1000):
    print(f'N[{i}] = {contador}')
    contador += 1
    if contador >= n:
        contador = 0 