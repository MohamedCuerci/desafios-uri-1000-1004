


n = int(input())


for i in range(n):
    poder = input()

    contagem = 0
    a = 0
    a1 = 0
    ka = 'k'

    for x in range(len(poder)):
        if poder[x] == 'k':
            a = contagem
            contagem = 0
        elif poder[x] == 'a':
            contagem += 1

    a1 = contagem
    a2 = a1 * a

    for x in range(a2):
        ka += 'a'
    print(ka)
