#codigo, qtde = input('numero: ').split()
codigo = input('codigo: ')
qtde = input('qtde: ')

codigo = int(codigo)
qtde = int(qtde)


if codigo == 1:
    valor = qtde * 4
elif codigo == 2:
    valor = qtde * 4.5
elif codigo == 3:
    valor = qtde * 5
elif codigo == 4:
    valor = qtde * 2
elif codigo == 5:
    valor = qtde * 1.5
    
#print(f'Total: R${valor:.2f}')
print('Total: R${:.2f}'.format(valor))