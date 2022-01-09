# num primo 
# https://www.pythonprogressivo.net/2018/06/Primos-Python-Como-Saber-Numero-e-Primo.html

n = int(input('dale: '))

for i in range(1, n+1):
    num = int(input('tropa: '))
    multiplos = 0

    for y in range(2, num):
        if num % y == 0:
            multiplos += 1
            #print(f'{num} nao eh primo')
    
    if multiplos == 0:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')