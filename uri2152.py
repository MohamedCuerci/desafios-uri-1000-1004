

n = int(input())

for i in range(n):
    h, m, o = input().split()

    h = int(h)
    m = int(m)
    o = int(o)

    digito = o


    if digito == 1:
        if h < 10 and m < 10:
            print(f'0{h}:{m} - A porta abriu!')
        if h < 10:
            print(f'0{h}:0{m} - A porta abriu!')
        else:
            print(f'{h}:{m} - A porta abriu!')
    else:
        if h < 10 and m < 10:
            print(f'0{h}:{m} - A porta fechou!')
        if h < 10:
            print(f'0{h}:0{m} - A porta fechou!')
        else:
            print(f'{h}:{m} - A porta fechou!')
