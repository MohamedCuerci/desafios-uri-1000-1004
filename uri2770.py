

# da certo mas o uri diz q o tempo foi excedido
while True:
    try:
        x, y, m = input().split()

        x = int(x)
        y = int(y)
        m = int(m)

        for i in range(m):
            a, b = input().split()

            a = int(a)
            b = int(b)

            if (a <= x and b <= y) or (b <= x and a <= y):
                print('Sim')
            else:
                print('Não')
    except:
        break






