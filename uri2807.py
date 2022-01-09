n = int(input())

ultimo=1
penultimo=1

if (n==1):
    print("1")
elif n == 2:
    print('1 1')
else:
    fibo = [1, 1]
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        fibo.append(termo)
    x = ''
    for numero in fibo:
        x += str(numero)
        x += ' '
    print(x[::-1].strip())