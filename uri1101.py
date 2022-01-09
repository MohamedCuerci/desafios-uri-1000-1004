while True:
    a, b = input().split()
    soma=0
    a = int(a)
    b = int(b)
    

    if a == 0 or b == 0:
        break

    elif a > b:
        for num in range(b, a+1):
            soma += num
            print(f'{num}' + " ", end='')
        print(f'Sum={soma}')
                
    elif b > a:
        for num in range(a, b+1):
            soma += num
            print(f'{num}' + " ", end='')
        print(f'Sum={soma}')
            