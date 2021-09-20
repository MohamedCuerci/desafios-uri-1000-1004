maior = 0
posi = 0

for n in range (1, 101):
    valor = int(input())

    if (maior < valor):
        maior = valor
        posi = n

print (maior)
print (posi)
