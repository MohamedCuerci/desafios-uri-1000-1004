

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a - b == 0 or a - c == 0 or b  - c == 0:
    print('S')
elif (a + b) - c == 0 or (a + c) - b == 0 or (b + c) - a == 0:
    print('S')
else:
    print('N')