
n = int(input())

for i in range(n):
    nome = input()
    x = nome.lower()

    vogais = ['a','e','i','o','u']
    consoantes = 0
    bandeira = True
    contagem = 0
    for letra in x:
        if letra not in vogais:
            consoantes += 1
            if consoantes == 3:
                #contagem += 1
                bandeira = False
        if letra in vogais:
            consoantes *= 0
        contagem += 1
    if contagem == len(nome) and bandeira == True:
        print(f'{nome} eh facil')
    else:
        print(f'{nome} nao eh facil')











