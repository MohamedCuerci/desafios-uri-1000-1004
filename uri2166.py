


def raizQuadradaDois(n):
    if n == 0:
        return 2
    x = 2+1/raizQuadradaDois(n-1)
    return x

n = int(input())
x = raizQuadradaDois(n)-1

print(f'{x:.10f}')