

# @ = a
# & = e
# ! = i
# * = o
# # = u  

while True:
    try:
        frase = input()
        
        frase_modificada = ''
        for letra in frase:
            if letra == '@':
                frase_modificada += 'a'
            elif letra == '&':
                frase_modificada += 'e'
            elif letra == '!':
                frase_modificada += 'i'
            elif letra == '*':
                frase_modificada += 'o'
            elif letra == '#':
                frase_modificada += 'u'
            else:
                frase_modificada += letra
        
        print(frase_modificada)

    except:
        break

