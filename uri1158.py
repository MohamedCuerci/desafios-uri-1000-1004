
x = 0
while True:
    x = input()

    x= int(x)
    if x == 0:
        break

    #x,y=a
    #x= int(x)
    #y=int(y)
    
    soma = 0
    j = 1

    while j <= 5:
        if x % 2 == 0:
            soma = soma + x
            x = x + 1
            j = j + 1
        
        if x % 2 != 0:
            x = x + 1
    print(soma)

