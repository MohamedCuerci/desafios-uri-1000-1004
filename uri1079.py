
# O arquivo de entrada contém um valor inteiro N na primeira linha. 
# Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

x = int(input('dale: '))

for i in range(x):
    v1, v2, v3 = input('dele: ').split()
    v1 = float(v1)
    v2 = float(v2)
    v3 = float(v3)
    soma = ((v1*2) + (v2*3) + (v3*5)) / 10
    print(f'{soma:.1f}')