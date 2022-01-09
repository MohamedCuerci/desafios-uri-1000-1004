


frase = input().split()

for letra in frase:
    if letra[0:2] == letra[2:4]:
        #letra == letra[2:]
        print(f'{letra[2:]}' + ' ', end='')
    else:
        print(f'{letra}' + " ", end='')









