n = float(input())

n100 = n // 100
n = n - n100*100

n50 = n // 50
n = n - n50*50

n20 = n // 20
n = n - n20*20

n10 = n // 10
n = n - n10*10

n5 = n // 5
n = n - n5*5

n2 = n // 2
n = n - n2*2

n1 = n // 1
n = n - n1*1

n050 = n // 0.5
n = n - n050*0.5

n025 = n // 0.25
n = n - n025*0.25

n010 = n // 0.10
n = n - n010*0.10

n05 = n // 0.05
n = n - n05*0.05

n01 = n // 0.01
n = n - n01*0.01

print('NOTAS:')
print(f'{int(n100)} nota(s) de R$ 100.00')
print(f'{int(n50)} nota(s) de R$ 50.00')
print(f'{int(n20)} nota(s) de R$ 20.00')
print(f'{int(n10)} nota(s) de R$ 10.00')
print(f'{int(n5)} nota(s) de R$ 5.00')
print(f'{int(n2)} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{int(n1)} moeda(s) de R$ 1.00')
print(f'{int(n050)} moeda(s) de R$ 0.50')
print(f'{int(n025)} moeda(s) de R$ 0.25')
print(f'{int(n010)} moeda(s) de R$ 0.10')
print(f'{int(n05)} moeda(s) de R$ 0.05')
print(f'{int(n01)} moeda(s) de R$ 0.01')

