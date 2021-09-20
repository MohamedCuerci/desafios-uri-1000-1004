contPar = 0
contImpar = 0
contPos = 0
contNeg = 0

for a in range (5):
    n = float(input())
    if (n % 2 == 0):
        contPar += 1
    else:
        contImpar += 1
    if (n > 0):
        contPos += 1
    elif (n < 0):
        contNeg += 1

print (f"{contPar} valor(es) par(es)")
print (f"{contImpar} valor(es) impar(es)")
print (f"{contPos} valor(es) positivo(s)")
print (f"{contNeg} valor(es) negativo(s)")

