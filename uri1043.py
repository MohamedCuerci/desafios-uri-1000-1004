
a, b ,c = input('xama: ').split()

a = float(a)
b = float(b)
c = float(c)

#variaveis perimetro triangulo 
perimetro = a + b + c
if ((a + b) > c) and ((a + c) > b) and ((b + c) > a) :
    print(f'Perimetro = {perimetro}')

else:    
#variavel trapezio 
    area = ((a + b) * c) / 2
    print(f'Area = {area}')






