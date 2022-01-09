
from iteration_utils import duplicates

lista = []
while True:
    nome = input("Digite um nome qualquer ou pressione <ENTER> para finalizar: ")
    if nome == "":
        break
    else:
        lista.append(nome)

    
print()
print(f'Tamanho da lista: {len(lista)}')

x = list(set(lista))
print(f'Nomes unicos: ')
for i in lista:
    print(i)

print()
print(f'Nomes repetidos: ')