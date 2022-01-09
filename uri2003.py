

while True:
    try:
        hora, minuto = input().split(':')
    
        horaM = (int(hora)) + 1
        minutoM = int(minuto)


        horaFinal = horaM - 8

        if horaFinal < 0:
            print('Atraso maximo: 0')
        else:
            minutoM += 60 * horaFinal
            print(f'Atraso maximo: {minutoM}')
    except:
        break