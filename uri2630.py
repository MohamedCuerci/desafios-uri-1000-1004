
""" n = int(input())

contador = 0
for i in range(n):
    x = input()
    lista = list(map(int,input().split()))

    menor = min(lista)
    mean = (sum(lista) / 3)
    eye = (lista[0] * 0.3) + (lista[1] * 0.59) + (lista[2] * 0.11)

    if  x == 'min':
        print(f'Caso #{contador}: {int(menor)}')

    elif x == 'mean':
        print(f'Caso #{contador}: {int(mean)}')

    else:
        print(f'Caso #{contador}: {int(eye)}') """

n = int(input())

for i in range(n):
 tipo = input()
 rgb = list(map(int,input().split()))

 if tipo == 'eye':
  r = int(0.3*rgb[0] + 0.59*rgb[1] + 0.11*rgb[2])
 elif tipo == 'mean':
  r = sum(rgb)//3
 elif tipo == 'max':
  r = max(rgb)
 else:
  r = min(rgb)

 print("Caso #{}: {}".format(i+1, r))