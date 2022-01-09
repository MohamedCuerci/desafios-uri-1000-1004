# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

v1 = int(input())
v2 = int(input())

somaImpar = 0

if v1 > v2:
    maior = v1
    for i in range(v2+1, v1):
        #print(i)
        if i % 2 != 0:
            somaImpar += i
else:
    maior = v2
    for i in range(v1+1, v2):
        if i % 2 != 0:
            somaImpar += i

print((somaImpar))



