
def fibo(n):
    ultimo = 1
    penultimo = 1
    if (n==1) or (n==2):
        return 1
    else:
        count=3
        while count <= n:
            dale = ultimo + penultimo
            penultimo = ultimo
            ultimo = dale
            count += 1
        return dale

nu = int(input())

for i in range(nu):
    n = int(input())
    if n == 0:
        print(f'Fib({n}) = 0')
    else:
        x = fibo(n)
        print(f'Fib({n}) = {x}')
    