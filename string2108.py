
#preciso conseguir achar a maior palavra mas codigo ja ta quase pronto

maior = 0
while True:
    palavra_inicial = input()
    y = palavra_inicial.split()

    if palavra_inicial == '0':
        break
    else:
        palavra_transformada = ''
        for palavra in y:
            tamanho = len(palavra)
            if tamanho >= maior:
                maior_maior = palavra
                maior = tamanho
            palavra_transformada += str(tamanho)
            palavra_transformada += '-'
            
        #palavras transoformadas em numero e separadas por '-' ja finalizada 
        x = palavra_transformada[:-1]
        print(x)

print()
print(f'The biggest word: {maior_maior}')



