n = int(input())

#ano = 2015

for i in range(n):
    data = int(input())

    tempo = data - 2015
    
    if tempo < 0:
        print(f'{abs(tempo)} D.C.')
    else:
        print(f'{(tempo+1)} A.C.')