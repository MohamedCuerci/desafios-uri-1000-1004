



""" while True:
    try:
        x = input()

        if x == 'as duas':
            print('caiu')
            break
        elif x == 'esquerda':
            print('ingles')
        elif x == 'direita':
            print('frances')
        else:
            print('portugues')
    except EOFError:
        break """

while True:
    try:
        c = input()
        if c == 'esquerda':
            print('ingles')
        elif c == 'direita':
            print('frances')
        elif c == 'nenhuma':
            print('portugues')
        elif c == 'as duas':
            print('caiu')

    except EOFError:
        break


