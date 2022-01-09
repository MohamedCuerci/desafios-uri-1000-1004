# questão certa mas uri da erro

qtde = 0
vI = 0
vG = 0
empate = 0

while True:
    g1, g2 = input('dale: ').split()
    g1 = int(g1)
    g2 = int(g2)
    qtde += 1
    if g1 > g2:
        vI += 1 
    elif g2 > g1:
        vG +=1
    else:
        empate += 1
    x = input('Novo grenal (1-sim 2-nao)')
    if x == '2':
        break
    else:
        pass

print(f'{qtde} grenais')
print(f'Inter:{vI}')
print(f'Gremio:{vG}')
print(f'empates:{empate}')

if g1 > g2:
    print('Inter venceu mais')
elif g2 > g1:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')




