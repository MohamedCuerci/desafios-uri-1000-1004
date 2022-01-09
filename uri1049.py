'''
p1 = input('')
p2 = input('')
p3 = input('')

if p1 == 'vertebrado':
    if p2 == 'ave':
        if p3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if p3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if p2 == 'inseto':
        if p3 == 'hematofogo':
            print('pulga')
        else:
            print('lagarta')
    else:
        if p3 == 'hematofogo':
            print('sanguessuga')
        else:
            print('minhoca')'''


tipo1 = input()
tipo2 = input()
tipo3 = input()

if tipo1 == 'vertebrado' and tipo2 == 'ave' and tipo3 == 'carnivoro':
    resul = 'aguia'

elif tipo1 == 'vertebrado' and tipo2 == 'ave' and tipo3 == 'onivoro':
    resul = 'pomba'

elif tipo1 == 'vertebrado' and tipo2 == 'mamifero' and tipo3 == 'onivoro':
    resul = 'homem'

elif tipo1 == 'vertebrado' and tipo2 == 'mamifero' and tipo3 == 'herbivoro':
    resul = 'vaca'

elif tipo1 == 'invertebrado' and tipo2 == 'inseto' and tipo3 == 'hematofago':
    resul = 'pulga'

elif tipo1 == 'invertebrado' and tipo2 == 'inseto' and tipo3 == 'herbivoro':
    resul = 'lagarta'

elif tipo1 == 'invertebrado' and tipo2 == 'anelideo' and tipo3 == 'hematofago':
    resul = 'sanguessuga'

elif tipo1 == 'invertebrado' and tipo2 == 'anelideo' and tipo3 == 'onivoro':
    resul = 'minhoca'

print(resul)




