
####################################

# MESMO CODIGO DA 1273 POREM O MEU DA ERRO MESMO ESTANDO TUDO CERTO

########################################

""" while True:
    n = int(input())
    if n == 0:
        break

    lista = []
    for i in range(n):
        lista.append(' '.join(input().split()))
    tamanho = max(len(i) for i in lista)

    print()
    for y in range(len(lista)):
        for j in range(tamanho-len(lista[y])):
            print('', end=' ')

        print(lista[y])
    print() """

check = 0
while True:
    n = int(input())
    if n == 0:
        break
    if check == 1:
        print()
        
    l = []
    for i in range(n):
        l.append(' '.join(input().split()))
    m = max(len(i) for i in l)

    for i in range(len(l)):
        for j in range(m-len(l[i])):
            print('', end=' ')

        print(l[i])
  

    check = 1