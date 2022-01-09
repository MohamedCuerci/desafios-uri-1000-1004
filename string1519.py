

#estou fazendo errado mas metade do caminho ja foi
#preciso separar e ordenar por ordem alfabetica

while True:
    frase = input().split()

    vogais = ['a','e','i','o','u']
    if frase == '.':
        break
    
    contador = 0
    frase_curta = ''
    lista_resumo = []
    for palavra in frase:
        if palavra[0] not in vogais:
            frase_curta += palavra[0]+'.'
            frase_curta += ' '
            contador += 1
        else:
            frase_curta += palavra
    print(frase_curta)
    print(contador)
    
    
    
















