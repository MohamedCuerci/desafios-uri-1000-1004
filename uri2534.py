
while True:
    try:
        notas, pessoas = input().split()

        notas = int(notas)
        pessoas = int(pessoas)

        lista = []

        for i in range(notas):
            teste = int(input())
            lista.append(teste)
            lista.sort(reverse=True)


        for i in range(pessoas):
            ordem = int(input())
            print(lista[ordem-1])
    except:
        break










