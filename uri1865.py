
num = int(input('dale: '))

for i in range(1, num+1):
    nome, força = input('nome e força: ').split()
    if nome == 'Thor':
        print('Y')
    else:
        print('N')