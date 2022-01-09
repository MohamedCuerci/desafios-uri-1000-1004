
""" n = int(input())

for i in range(n):
    nn = int(input())

    #contadoras 
    portuguess = 0
    chiness = 0
    espanholl = 0
    contagem = 0

    for y in range(nn):
        idioma = input()

        if idioma == 'portugues':
            portuguess += 1
            if portuguess == nn:
                print('portugues')
        if idioma == 'chines':
            chiness += 1
            if chiness == nn:
                print('chines')
        if idioma == 'espanhol':
            espanholl += 1
            if espanholl == nn:
                print('espanhol')
        contagem += 1

        if contagem == nn:
            if portuguess >= 1 and chiness >= 1 or portuguess >= 1 and espanholl >=1 or espanholl >= 1 and chiness >= 1:
                print('ingles')  """ 


n = int(input())
while(n > 0):
    n -= 1
    l = []
    m = int(input())
    while(m > 0):
        m -= 1
        l.append(input())
    main = l[0]
    for m in l:
        if m != main:
            main = 'ingles'
            break
    print(main)






