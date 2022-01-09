
while True:
    try:
        n = int(input())
        maior = 0
        for i in range(n):
            tempo, distancia = input().split()
            tempo = int(tempo)
            distancia = int(distancia)

            if distancia/tempo > maior:
                print(i+1)
                maior = distancia/tempo

    except:
        break








