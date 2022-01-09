
# 2 notas depois e media depois delas   


i = 0
media = 0

while i < 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        i += 1
        media += nota
    if nota < 0 or nota > 10:
        print('nota invalida')

media = media / 2

print(f'media = {media}')
