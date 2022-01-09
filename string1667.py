
#quase consegui


while True:
    try:
        x = 80*'-'
        frase = input()
        if len(frase) <= 80:
            if '<br>' in frase:
                x1 = '<br>'
                frase = frase.replace(x1, '\n')
                dale = frase
            if '<hr>' in frase:
                x2 = '<hr>'
                dale = frase.replace(x2, x)
            print(f'{frase}')
        else:
            if '<br>' in frase:
                x1 = '<br>'
                if frase[0:4] == '<br>':
                    print()
                    frase = frase.replace(x1, '\n')
                    dale = frase
            if '<hr>' in frase:
                x2 = '<hr>'
                dale = frase.replace(x2, x)
            print(f'{frase}\n')

    except EOFError:
        break