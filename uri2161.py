


def raizQuadradaDez(n):
    if n == 0:
        return 6
    x = 6+1/raizQuadradaDez(n-1)
    return x

n = int(input())
x = raizQuadradaDez(n)-3

print(f'{x:.10f}')