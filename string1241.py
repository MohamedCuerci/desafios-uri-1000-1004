n = int(input(''))

for i in range(1, n+1):
    a, b = input().split()

    if b in a:
        print('encaixa')
    if b not in a:
        print('nao encaixa')
