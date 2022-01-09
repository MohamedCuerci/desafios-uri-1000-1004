
x = int(input('dale: '))

for i in range(x):
    palavra = input('palavra: ')

    if len(palavra) == 3:
        x1 = palavra[0]
        x2 = palavra[1]
        x3 = palavra[2]
        if x1 =='o' and x2 == 'n' or x1 == 'o' and x3 == 'e' or x2 == 'n' and x3 == 'e':
            print('1')
        if x1 =='t' and x2 == 'w' or x1 == 't' and x3 == 'o' or x2 == 'w' and x3 == 'o':
            print('2')
    else:
        print('3')