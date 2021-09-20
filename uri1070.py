n = int(input())

if (n % 2 == 0):
    for a in range(n+1, n+12, 2):
        print(a)

else:
    for a in range(n, n+12, 2):
        print(a)