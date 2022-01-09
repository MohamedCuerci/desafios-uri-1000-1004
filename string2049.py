
#meu codigo esta cert porem o uri não aceita
""" contador = 0 
while True:
    assinatura = input()
    if assinatura == '0':
        break
    else:
        contador += 1
        print(f'Instancia {contador}')
        algarismos = input()

        if assinatura in algarismos:
            v = 'verdadeiro'
        else:
            v = 'falsa'
        print(f'{v}')
        print()
 """

i = 1
while True:
    a = input()
    if a == '0':
        break
    if i != 1:
        print()
    painel = input()
    print('Instancia %d' % i)
    i += 1
    if a in painel:
        print('verdadeira')
    else:
        print('falsa')