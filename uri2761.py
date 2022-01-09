
""" x = input().split()

a = int(x[0])
b = float(x[1])
c = str(x[2])
d = ' '.join(x[3:])


print(f'{a}{b}{c}{d}')
print(f'{a}\t{b}\t{c}\t{d}')
print(f'{a:^10}{b:^10.6f}{c:^10}{d:^10}') """


entrada = input().split()
inteiro = int(entrada[0])
real = float(entrada[1])
caracter = entrada[2]
frase = ' '.join(entrada[3:])
tudo = ''.join(entrada)
print('%s' % tudo)
print('%d\t%f\t%c\t%s' % (inteiro, real, caracter, frase))
print('%10d%10.6f%10c%10s' % (inteiro, real, caracter, frase))



















