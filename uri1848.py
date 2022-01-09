
contador = 0
p = 0
dale = True
while dale:
    x = input()
    if x != 'caw caw':
        if x == '--*':
            contador += 1
        elif x == '*--':
            contador += 4
    else:
        print(contador)
        p += 1
        if p == 3:
            break

print(contador)