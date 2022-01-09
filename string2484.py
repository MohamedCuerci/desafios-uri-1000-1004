""" p = input()

palavra = ''
#criando a palavra inteira com espaços
for letra in p:
    palavra += letra
    palavra += ' '

print(f'{palavra:^}') """

while True:
    try:
        palavra = input()
        l = []
        for i in palavra:
            l.append(i)
        tamanho = len(l)

        for y in range(tamanho):
            for z in range(y):
                print('', end=' ')
                
            for j in range(tamanho):
                print(l[j], end='')
                if(j != tamanho-1):
                    print(' ', end='')
            print('')
            tamanho -= 1

        print('')
           
    except EOFError:
        break
