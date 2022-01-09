

n = int(input())

for i in range(n):
    contador = 1
    frase = input()

    for letra in frase:
        #contador += 1
        if letra.upper() == 'A' or letra.upper() == 'E' or letra.upper() == 'I' or letra.upper() == 'O' or letra.upper() == 'S':
            contador *= 3
        else:
            contador *= 2

    print(contador)
