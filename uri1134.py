# 1 = alcool 
# 2 - gasolina
# 3 - diesel
# 4 - fim

alcool = 0
gasolina = 0
diesel = 0

x = 0
while x != 4:
    x = int(input('dale: '))
    if x == 1:
        alcool += 1
    elif x == 2:
        gasolina += 1
    elif x == 3:
        diesel += 1

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
