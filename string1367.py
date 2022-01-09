
# preciso coninuar to quase



while True:
    parada = int(input())

    if parada == 0:
        break

    correto = 0
    incorreto = 0    
    b1 = 0
    for i in range(parada):
        a, b, c = input().split()

        b = int(b)

        if c == 'correct':
            correto += 1
            b1 += b
        else:
            incorreto += 1
        
    if incorreto < correto and incorreto >= 1:
        b1 += 20

    print(f'{correto} {b1}')










