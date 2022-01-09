
while True:
    try:
        frase = input()
        fraseEditada = ''
        bandeira = True
        bandeira1 = True

        for letra in range(len(frase)):

            if frase[letra] == '_':
                if bandeira:
                    fraseEditada += '<i>'
                    bandeira = False
                else:
                    fraseEditada += '</i>'
                    bandeira = False

            elif frase[letra] == '*':
                if bandeira:
                    fraseEditada += '<b>'
                    bandeira1 = False
                else:
                    fraseEditada += '</b>'
                    bandeira1 = True

            else:
                fraseEditada += frase[letra]

        print(fraseEditada)

    except EOFError:
        break
























