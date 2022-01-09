
lista = []
while True:
    try:
        nome = input()
        if nome == '':
            break
        else:
            lista.append(nome)  
       
    except EOFError:
        break

lista = sorted(lista, key=lambda s: s.lower())
print(lista[-1])





