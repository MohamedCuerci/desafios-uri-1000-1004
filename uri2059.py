

p, j1, j2, r, a = input('').split()

p = int(p)
j1= int(j1)
j2 = int(j2)
r = int(r)
a = int(a)


v = 0

if (j1 + j2) % 2 == 0:
    if p == 1:
        v = 1
    else:
        v = 2
else:
    if p == 0:
        v = 1
    else:
        v = 2


if r == 1 and a == 1:
    print('Jogador 2 ganha!')
elif r == 1 and a == 0:
    print('Jogador 1 ganha!')
elif r == 0 and a == 1:
    print('Jogador 1 ganha!')
elif r == 0 and a == 0:
    if v == 1:
        print('Jogador 1 ganha!')
    elif v == 2:
        print('Jogador 2 ganha!')