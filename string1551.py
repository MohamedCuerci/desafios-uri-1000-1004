alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

n = int(input())

for i in range(n):
    frase = input()
    total = 0
    letras_usadas = []
    for letra in frase:
        if letra not in letras_usadas:
            letras_usadas.append(letra)   
            if letra in alfabeto:
                total += 1

    if total == 26:
        print('frase completa')
    elif total >= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
    

        
   

















