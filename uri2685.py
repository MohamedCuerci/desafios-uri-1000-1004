

while True:
    try:
        n = int(input())

        if n >= 0 and n <= 45  or n >= 316 and n <= 360:
            print('Bom Dia!!')
        if n >= 46 and n <= 135 :
            print('Boa Tarde!!')
        if n >= 136 and n <= 225:
            print('Boa Noite!!')
        if n >= 226 and n <= 315:
            print('De Madrugada!!')

    except:
        break