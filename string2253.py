while True:
    try:
        senha = input()
        #flags
        minusculas = False
        maiusculas = False
        espaços = False
        numero = False

        tamanho = len(senha)

        if senha != '':
            for i in range(len(senha)):
                if ord(senha[i]) > 64 and ord(senha[i]) < 91:
                    maiusculas = True
                elif ord(senha[i]) > 96 and ord(senha[i]) < 123:
                    minusculas = True
                elif ord(senha[i]) > 47 and ord(senha[i]) < 58:
                    numero = True
                elif senha[i].isspace():
                    espaços = True
            
            if tamanho >= 6 and tamanho <= 32:
                if(maiusculas and minusculas and numero and espaços == False):
                    print('Senha valida.')
                else:
                    print('Senha invalida.')
            else:
                print('Senha invalida.')
        else:
            break

    except EOFError:
        break