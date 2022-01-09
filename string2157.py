
frase = int(input())
for i in range(frase):
    final = ""
    contrario = ""
    
    a, b = input().split()
    a = int(a)
    b = int(b)

    while a <= b:
        final += str(a)
        a += 1

    contrario = final + final[::-1]
    print(contrario)


