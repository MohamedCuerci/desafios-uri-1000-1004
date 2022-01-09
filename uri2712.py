
m = ['ABCDEFGHIJKLMNOPQRSTUVXWYZ']
n = int(input())


for i in range(n):
    placa = input().split('-')
    while True:
            x = placa[0]
            y = placa[1]
            if (len(placa) == 2) and (len(placa[0]) == 3) and (len(placa[1]) == 4) and (placa[0] == placa[0].upper()):
                try:
                    if y[-1] == '1' or y[-1] == '2':
                        print('MONDAY')
                        break
                    elif y[-1] == '3' or y[-1] == '4':
                        print('TUESDAY')
                        break
                    elif y[-1] == '5' or y[-1] == '6':
                        print('WEDNESDAY')
                        break
                    elif y[-1] == '7' or y[-1] == '8':
                        print('THURSDAY')
                        break
                    elif y[-1] == '9' or y[-1] == '0':
                        print('FRIDAY')
                        break
                    else:
                        print('FAILURE')
                        break
                except:
                    print('FAILURE')
                    break


