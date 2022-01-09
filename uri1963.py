
#diferença percentual entre 2 valores

valorA, valorB = input().split()

valorA = float(valorA)
valorB = float(valorB)

diferenca = ((valorB * 100)/ valorA) - 100.00

print(f'{diferenca:.2f}%')


