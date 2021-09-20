'''a = float(input('fala comigo: '))
#a = float(a)

novoS0 = a + a * (15/100)
novoS1 = a + a * (12/100)
novoS2 = a + a * (10/100)
novoS3 = a + a * (7/100)
novoS4 = a + a * (4/100)
ganhoMais0 = novoS0 - a
ganhoMais1 = novoS1 - a
ganhoMais2 = novoS2 - a
ganhoMais3 = novoS3 - a
ganhoMais4 = novoS4 - a
#perc = 

if a<=400:
    print(f'Novo salario: {novoS0:.2f}')
    print(f'Reajuste ganho: {ganhoMais0}')
    print('Em percentual: 15 %')

elif (a>=400.01) and (a<=800):
    print(f'Novo salario: {novoS1:.2f}')
    print(f'Reajuste ganho: {ganhoMais1}')
    print('Em percentual: 12 %')

elif (a>=800.01) and (a<=1200):
    print(f'Novo salario: {novoS2:.2f}')
    print(f'Reajuste ganho: {ganhoMais2:.2f}')
    print('Em percentual: 10 %')

elif (a>=1200.01) and (a<=2000):
    print(f'Novo salario: {novoS3:.2f}')
    print(f'Reajuste ganho: {ganhoMais3:.2f}')
    print('Em percentual: 7 %')

elif a > 2000.00:
    print(f'Novo salario: {novoS4:.2f}')
    print(f'Reajuste ganho: {ganhoMais4:.2f}')
    print('Em percentual: 4 %')'''


'''a = float(input())


if a <= 400.00:
    s = a * 1.15
    r = s - a
    p = 15
if 400.01 <= a <= 800.00:
    s = a * 1.12
    r = s - a
    p = 12
if 800.01 <= a <= 1200.00:
    s = a * 1.10
    r = s - a
    p = 10
if 1200.01 <= a <= 2000.00:
    s = a * 1.07
    r = s - a
    p = 7
if  a > 2000.00:
    s = a * 1.04
    r = s - a
    p = 4
    
print(f'Novo salario: {s:.2f}')
print(f'Reajuste ganho: {r:.2f}')
print(f'Em percentual: {p} %')'''    


Salário = float(input('salario: '))
    
if((Salário >= 0) and (Salário <= 400)):
    print(f'Novo salario: {Salário * 15/100 + Salário}\nReajuste ganho: {Salário * 15/100}\nEm percentual: {15} %')
elif((Salário >= 400.01) and (Salário <= 800)):
    print(f'Novo salario: {round(Salário * 12/100 + Salário, 2)}\nReajuste ganho: {round(Salário * 12/100, 2)}\nEm percentual: {12} %')
elif((Salário >= 800.01) and (Salário <= 1200)):
    print(f'Novo salario: {round(Salário * 10/100 + Salário, 2)}\nReajuste ganho: {round(Salário * 10/100, 2)}\nEm percentual: {10} %')
elif((Salário >= 1200.01) and (Salário <= 2000)):
    print(f'Novo salario: {round(Salário * 7/100 + Salário, 2)}\nReajuste ganho: {round(Salário * 7/100, 2)}\nEm percentual: {7} %')
else:
    if(Salário > 2000):
        print(f'Novo salario: {round(Salário * 4/100 + Salário, 2)}\nReajuste ganho: {round(Salário * 4/100, 2)}\nEm percentual: {4} %')