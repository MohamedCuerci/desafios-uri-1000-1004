
n = int(input())

for i in range(n):
    p1, e1, p2, e2 = input().split()
    num1, num2  = input().split()

    num1 = int(num1)
    num2 = int(num2)

    #e1 = int(e1)
    #e2 = int(e2)

    resultado = num1 + num2
    if resultado % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

    if resultado == e1:
        print(p1)
    else:
        print(p2)
