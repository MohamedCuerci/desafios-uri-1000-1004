

x = int(input('dale: '))

dentro = 0
fora = 0

for i in range(x):
    y = int(input('dele: '))
    if y >=10 and y <= 20:
        dentro += 1
    else:
        fora += 1

print(f'{dentro} in')
print(f'{fora} in')