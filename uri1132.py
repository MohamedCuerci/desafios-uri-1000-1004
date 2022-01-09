
# multiplos de 13


x, y = input('dale: ').split()

x = int(x)
y = int(y)

soma = 0

if x > y:
    for i in range(y, x+1):
        if i % 13 == 0:
            #foda-se kkkk
            pass
        else:
            soma += i
if x < y:
    for i in range(x, y+1):
        if i % 13 == 0:
            #foda-se kkkk
            pass
        else:
            soma += i

print(soma)
