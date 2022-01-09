x = int(input())

for i in range(1, x+1):
    n = int(input('dale: '))
    if n > 0 and n % 2 == 0:
        print('EVEN POSITIVE')
    elif n < 0 and n % 2 == 0:
        print('EVEN NEGATIVE')
    elif n < 0 and n % 2 != 0:
        print('ODD NEGATIVE')
    elif n > 0 and n % 2 != 0:
        print('ODD POSITIVE')
    else:
        print('NULL')



