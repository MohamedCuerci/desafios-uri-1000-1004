""" n = float(input())

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
 """

text = "nota(s) de R$"
text1 = "moeda(s) de R$"
valor = float(input())
n100 = valor// 100
valor -= n100 * 100
n50 = valor// 50
valor -= n50 * 50
n20 = valor// 20
valor -= n20 * 20
n10 = valor// 10
valor -= n10 * 10
n5 = valor// 5
valor -= n5 * 5
n2 = valor// 2
valor -= n2 * 2
n1 = valor// 1
valor -= n1 * 1
n05 = valor// 0.5
valor -= n05 * 0.5
n025 = valor// 0.25
valor -= n025 * 0.25
n010 = valor// 0.1
valor -= n010 * 0.1
n005 = valor// 0.05
valor -= n005 * 0.05
n001 = valor// 0.01
valor -= n001 * 0.01

print("NOTAS: ")
print(f"{n100} {text} 100.00")
print(f"{n50} {text} 50.00")
print(f"{n20} {text} 20.00")
print(f"{n10} {text} 10.00")
print(f"{n5} {text} 5.00")
print(f"{n2} {text} 2.00")

print("MOEDAS:")
print(f"{n1} {text1} 1.00")
print(f"{n05} {text1} 0.50")
print(f"{n025} {text1} 0.25")
print(f"{n010} {text1} 0.10")
print(f"{n005} {text1} 0.05")
print(f"{n001} {text1} 0.01")
