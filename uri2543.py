

while True:
    try:
        n, id = input().split()
        n = int(n)
        total = 0
        for i in range(n):
            facul, jogo = input().split()

            jogo = int(jogo)
            
            if  facul == id and jogo == 0:
                total += 1
        print(total)
    except:
        break
