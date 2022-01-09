
#esse codigo nao da certo no uri, mas parece estar correto
#talvez seja palavras somam msm qaundo é formada apenas com simbolos
while True:
    try:
        frase = input().split()
        palavras = 0
        letras = 0
        for palavra in frase:
            palavras += 1
            for letra in palavra:
                if letra.isalpha():    
                    letras += 1

        tamanho = letras / palavras
        if tamanho <= 3:
            print(250)
        elif tamanho >=4 and tamanho <=5:
            print(500)
        else:
            print(1000)

    except EOFError:
        break





















