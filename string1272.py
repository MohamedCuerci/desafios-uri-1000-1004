

""" n = int(input())

for i in range(n):
    palavras = input().split('·')

    conjunto = ''
    for letra in palavras:
        conjunto += letra[0:1]
    print(conjunto) """


n = input()

for nIndex in range(n):
    palavras = input().split(' ')
    texto = ""

    for palavra in palavras:
        if palavra != '':
            texto += palavra[0]
    
    print(texto)