

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

l = input().lower()

contador = 1
for letra in alfabeto:
    if letra == l:
        print(contador)
    else:
        contador += 1
