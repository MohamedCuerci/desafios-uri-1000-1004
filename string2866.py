

n = int(input())

for i in range(n):
    quase = ''
    codigo = input()

    for letra in codigo:
        if letra.islower():
            quase += letra
    print(quase[::-1])







