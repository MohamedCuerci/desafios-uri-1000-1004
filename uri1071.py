v1 = int(input())
v2 = int(input())
soma = abs(v1) + abs(v2)
somaFinal = 0

for somaImpar in range(1,3):
    if soma % 2 != 0:
        somaFinal = int(soma / 2)

print((somaFinal))
