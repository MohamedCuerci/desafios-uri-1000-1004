
while True:
    try:
        frase_vazia = ''

        frase = input()

        contador = 0
        for letra in frase:
            if letra == ' ':
                frase_vazia += letra    
            elif contador % 2 == 0:
                frase_vazia += letra.upper()
                contador += 1
            else:
                frase_vazia += letra.lower()
                contador += 1

        print(frase_vazia)
    except EOFError:
        break


















