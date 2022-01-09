

x = int(input('dale: '))

for i in range(x):
    v1, v2 = input('bora: ').split()
    v1 = int(v1)
    v2 = int(v2)
    try:
        d = v1 / v2
        print(f'{d:.1f}')
    except ZeroDivisionError:
        print('divisao impossivel')