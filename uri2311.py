
# não achei nenhuma maneira de converter os numeros separados no split como float

n = int(input())

listaNotas = []
#listaNomes = []

for i in range(n):
    nomes = input()
    dificultade = float(input())
    notas = list(map(float,input().split()))

    notas.sort()
    notas = notas[1:6]
    
    resultado = sum(notas)*dificultade

    print(f'{nomes} {resultado:.2f}')






