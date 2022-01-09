
n = int(input())

animalC = 0
animalR = 0
animalS = 0

for i in range(1, n+1):

    num, animal = input().split()

    num = int(num)

# calculo dos animals 
    if animal == 'C':
        animalC += num
    if animal == 'R':
        animalR += num
    if animal == 'S':
        animalS += num

# porcentagem 

    total = animalC + animalR + animalS
    PanimalC = (animalC / total) * 100
    PanimalR = (animalR / total) * 100
    PanimalS = (animalS / total) * 100


print(f'Total: {total} cobaias')
print(f'Total de coelhos: {animalC}')
print(f'Total de ratos: {animalR}')
print(f'Total de sapos: {animalS}')
print(f'Percentual de coelhos: {PanimalC:.2f} %')
print(f'Percentual de ratos: {PanimalR:.2f} %')
print(f'Percentual de Sapos: {PanimalS:.2f} %')