
#esta dando erro mas a questão esta certa

r1, r2, r3 = input().split()

r1 = int(r1)
r2 = int(r2)
r3 = int(r3)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Valido-Equilatero')
    if r1 != r2 != r3 != r1:
        print('Valido-Escaleno')
    else:
        print('Valido-Isoceles')

    if((pow(r1,2)+pow(r2,2))==pow(r3,2)):
        retan = 'S'
    else:
        retan = 'N'
    print("Retangulo: ",retan)
else:
    print('Invalido')
