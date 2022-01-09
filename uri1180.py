



quantidade = int(input('Qtd: '))
numero = input().split()
int_lista = list(map(int, numero))

int_lista = int_lista[0:quantidade]

menor = min(int_lista)
indece = int_lista.index(menor)

print(f'Menor valor: {menor}')
print(f'Posicao: {indece}')

