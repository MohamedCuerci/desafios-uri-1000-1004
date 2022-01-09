n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)


notaP = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10
#dale = n3 * 3

print(f'Media: {notaP:.1f}')

if  notaP >= 7:
    print(f'Aluno aprovado.')

if notaP < 5:
    print(f'Aluno reprovado.')

if notaP >=5.1 and notaP <= 6.9:
    print(f'Aluno em exame.')
    notaExame = float(input())
    print(f'Nota do exame: {notaExame}')
    notaFinal = (notaP + notaExame) / 2
    if  notaFinal >= 5:
        print(f'Aluno aprovado.')
        print(f'Media final: {notaFinal:.1f}')
    else:
        print(f'Aluno reprovado.')
        print(f'Media final: {notaFinal:.1f}')
