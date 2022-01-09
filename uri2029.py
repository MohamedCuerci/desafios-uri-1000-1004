
# area cilindro


while True:
    try:
        volume = float(input())
        diametro = float(input())

        raio = diametro / 2
        area = 3.14 * (raio*raio)
        altura = volume / area

        print(f'ALTURA = {altura:.2f}')
        print(f'AREA = {area:.2f}')
    except:
        break