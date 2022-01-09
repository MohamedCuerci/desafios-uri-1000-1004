
salida = 0
vuelta = 0
d = 0

while True:
    try:
        n = input('').split()

        if n[0] == 'ABEND':
            break

        dale = n[0]
        p = int(n[1])

        if dale == 'SALIDA':
            salida += 1
            d += p
        if dale == 'VUELTA':
            vuelta += 1
            d -= p

        #diferenca = salida - vuelta
    except ValueError:
        break

diferenca = salida - vuelta

print(d)
print(diferenca)





