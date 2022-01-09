


n = int(input())

for i in range(n):
    a, b = input().split()
    x = int(a) ** int(b)
    x = str(x)
    print(len(x))