

#esta certo mas uri não aceita

n = int(input())

for i in range(n):
    frase = input().split()
    
    frase_manipulada = ''
    for palavra in frase:
        if len(palavra) > 8 and 'oulupukk' in palavra:
            if palavra[-1] == '.':
                frase_manipulada += 'Joulupukki.'
                #frase_manipulada += ' '
            else:
                frase_manipulada += 'Joulupukki'
                frase_manipulada += ' '
        else:
            frase_manipulada += palavra
            frase_manipulada += ' '

    print(frase_manipulada.strip())







