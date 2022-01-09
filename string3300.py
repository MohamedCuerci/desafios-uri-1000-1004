
numeros = input()

contador = 0
ultima_letra = ''
for n in numeros:
    if ultima_letra == '1' and n == '3':
        contador += 1
    ultima_letra = n

if contador > 0:
    print(f'{numeros} es de Mala Suerte')
else:
    print(f'{numeros} No es de Mala Suerte')