
soma = 0
vzs = 0
x = 0
while x >= 0:
    x = int(input('dale: '))
    if x >= 0:
        soma += x
        vzs += 1

print(f'{soma/vzs:.2f}')