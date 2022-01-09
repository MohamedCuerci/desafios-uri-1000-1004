
# preciso continuar
n = int(input())

frase = input().upper().split()

frase_modificada = ''
for palavra in frase:
    if len(palavra) == 3 and 'OB' in palavra:
        frase_modificada += 'OBI'
    elif len(palavra) == 3 and 'UR' in palavra:
        frase_modificada += 'URI'
    else:
        frase_modificada += palavra
    frase_modificada += ' '

print(frase_modificada)           






















