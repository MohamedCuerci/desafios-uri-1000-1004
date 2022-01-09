
renda = float(input('dale: '))


if renda <= 2000.00:
    imposto = 0
    print('Isento')
    
if 2000.00 < renda <= 3000.00:
    r8 = renda - 2000.00
    imposto = r8 * (8 / 100)
    
if 3000.00 < renda <= 4500.00:
    i8 = (8 / 100) * (1000.00)
    r18 = renda - 3000.00
    imposto = r18 * (18 / 100) + i8
    
if renda > 4500.00:
    i8 = (8 / 100) * (1000.00)
    i18 = (18 / 100) * (1500.00)
    r28 = renda - 4500.00
    imposto = i18 + i8 + r28 * (28 / 100)

if renda > 2000.00:
    imposto = float(imposto)
    print(f'R$ {imposto:.2f}')


