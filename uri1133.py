
a = int(input('dale: '))
b = int(input('dale:'))

a = int(a)
b = int(b)

if a > b:
    for num in range(b, a):
        if num % 5 == 2 or num % 5 == 3:
            print(num)
if a < b:
    for num in range(a, b):
        if num % 5 == 2 or num % 5 == 3:
            print(num)
