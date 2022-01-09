a, b, c, d, e, f, g, h, i = input().split()

total = int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h) + int(i)

parte1 = str(total)[0:1]
parte2 = str(total)[1:2]

x = int(parte1) + int(parte2)

if x <= 9:
    if x == 1:
        print('Dasher')
    elif x == 2:
        print('Dancer')
    elif x == 3:
        print('Prancer')
    elif x == 4:
        print('Vixen')
    elif x == 5:
        print('Comet')
    elif x == 6:
        print('Cupid')
    elif x == 7:
        print('Donner')
    elif x == 8:
        print('Blitzen')
    else:
        print('Rudolph')

else:
    x = str(x)

    parte3 = x[0:1]
    parte4 = x[1:2]

    y = int(parte3) + int(parte4)

    if y <= 9:
        if y == 1:
            print('Dasher')
        elif y == 2:
            print('Dancer')
        elif y == 3:
            print('Prancer')
        elif y == 4:
            print('Vixen')
        elif y == 5:
            print('Comet')
        elif y == 6:
            print('Cupid')
        elif y == 7:
            print('Donner')
        elif y == 8:
            print('Blitzen')
        else:
            print('Rudolph')





