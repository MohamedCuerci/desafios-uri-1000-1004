# cifra cesar 

vzs = int(input('qauntas vzs: '))
for i in range(vzs):
    texto = input('dale: ').upper()
    n = int(input('deslocação: '))
    #texto = input('dale: ').upper()
    textocifrado = ""
    #Utilizaremos uma string do alfabeto com suas respectivas posicoes dentro da lista para realizar a substituicao
    #alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCD"
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letra in texto:
        localizacao = alfabeto.find(letra)
        if localizacao >= 0:
            novaLocalizacao = localizacao - n
            if novaLocalizacao > 26:
                #realiza o enquadramento do caractere criptografado no inicio da lista
                #uma vez que so temos 26 caracteres
                novaLocalizacao = novaLocalizacao % 26
            #novaLocalizacao = localizacao + 3
            textocifrado += alfabeto[novaLocalizacao]
        else:
            textocifrado += letra

    print(textocifrado)






























'''n = int(input('deslocação: '))
texto = input('dale: ').upper()
textocifrado = ""
#Utilizaremos uma string do alfabeto com suas respectivas posicoes dentro da lista para realizar a substituicao
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCD"

for letra in texto:
    localizacao = alfabeto.find(letra)
    if localizacao >= 0:
        novaLocalizacao = localizacao + n
        if novaLocalizacao > 26:
            #realiza o enquadramento do caractere criptografado no inicio da lista
            #uma vez que so temos 26 caracteres
            novaLocalizacao = novaLocalizacao % 26
        #novaLocalizacao = localizacao + 3
        textocifrado += alfabeto[novaLocalizacao]
    else:
        textocifrado += letra

print(textocifrado)'''