
while True:
    try:
        n, minimo, maximo = input().split()

        n = int(n)
        maximo = int(maximo)
        minimo = int(minimo)

        total = 0
        for i in range(n):
            x = int(input())

            if x <= maximo and x >= minimo:
                total += 1
            else:
                pass

        print(total)
    except:
        break