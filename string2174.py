total = 151

lista = []

n = int(input())

for i in range(n):
    pokemon = input()
    lista.append(pokemon)

x = set(lista)
contador = 0
for i in x:
    contador += 1

print(f'Falta(m) {(total - contador)} pomekon(s).')