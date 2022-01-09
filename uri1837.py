


a, b = input('dale: ').split()

a = int(a)
b = int(b)

if b < 0:
    b =  abs(b)
    print(f'{-1*(a//b)} {a%b}')
else:
    print(f'{a//b} {a%b}')