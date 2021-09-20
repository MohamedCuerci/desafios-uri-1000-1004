cont = 0
soma = 0
for a in range(6):
    b = float(input("digite um numero: "))
    if b > 0:
        cont += 1
        soma += b
print(f"{cont} valores positivos")
print(f'{(soma/cont):.1f}')

cont = 0
soma = 0

for a in range (6):
    n = float(input())
    if n > 0:
        cont += 1
        soma += n
print (f"{cont} valores positivos")
print (f"{(soma/cont):.1f}")
