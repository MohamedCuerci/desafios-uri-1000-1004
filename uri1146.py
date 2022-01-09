# imprimir o i com espaços mas se for o ultimo não fazer isso

while True:
    n = int(input('dale: '))
    for i in range(1, n+1):
        #print(i)
        if i < n:
            print( str(i) + ' ', end='')
        if i == n:
            print(i)
    if n == 0:
        break





