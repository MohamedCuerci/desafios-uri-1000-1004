n = int(input('dale: '))

#soma = 0

for i in range(1, n+1):
    num = int(input('tropa: '))

    j = 1
    soma = 0
    
    # descobrindo se é divisor
    while j < num:
        if num % j == 0:
            soma += j
 
        j += 1

    if soma == num:
        print(f'{num} eh perfeito')

    else:
        print(f'{num} nao eh perfeito')
