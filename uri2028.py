
while True:
    try:
        caso = 1
        qtde = 1
        n = int(input())
        for y in range(n+1):
            qtde += y
        
        if qtde == 1:
            print(f'Caso {caso}: {qtde} numero')

        else:
            print(f'Caso {caso}: {qtde} numeros')

        if n == 0:
            print(0)
        else:
            print(0, end=' ')

        for i in range(n+1):
            for b in range(i):
                if i == n and b == n - 1:
                    print(i)
                else:
                    print(i, end=' ')
        
        print('')
        caso += 1
    except:
        break
