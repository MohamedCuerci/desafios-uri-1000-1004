
def cria_tabuleiro(tamanho):
    contador = 0
    par = 0
    impar = 0
    for linha in range(tamanho):
        for coluna in range(tamanho):
            contador += 1
            if contador % 2 == 0:
                par += 1
            else:
                impar += 1

    return impar, par

x = int(input(''))

impar, par = cria_tabuleiro(x)

print(f'{impar} casas brancas e {par} casas pretas')