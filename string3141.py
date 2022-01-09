
#ta quase preciso terminar ainda
#só preciso so raciocinio do mes e dia


nome = input()

nascD1, nascM1, nascA1 = input().split('/')
nascD2, nascM2, nascA2 = input().split('/')

nascA2 = int(nascA2)
nascA1 = int(nascA1)
nascD1 = int(nascD1)
nascD2 = int(nascD2)
nascM1 = int(nascM1)
nascM2 = int(nascM2)

anos = (nascA1 - nascA2)
if nascD1 == nascD2 and nascM1 == nascM2:
    print('Feliz aniversario!')
    anos += 1



        


print(f'Voce tem {anos} anos {nome}.')









