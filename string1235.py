
n = int(input())

for i in range(n):
    frase = input()

    metade = len(frase)/2
    metade = int(metade)
    
    primeira_metade = frase[:metade]
    segundo_metade = frase[metade:]

    x = primeira_metade[::-1]
    y = segundo_metade[::-1]

    print(f'{x}{y}')
















