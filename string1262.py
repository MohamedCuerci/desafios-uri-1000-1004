

while True:
    try:
        rw = input()
        p = int(input())
        total = 0
        contagem = p
        for i in range(len(rw)):
            if rw[i] == 'R':
                if contagem == p:
                    total += 1
                if contagem == 0:
                    contagem = p
                    total += 1
                contagem -= 1
            elif rw[i] == 'W':
                total += 1
                contagem = p
        print(total)

    except EOFError:
        break





























