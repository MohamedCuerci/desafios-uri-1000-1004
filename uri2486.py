
# recomendado 110 ~ 130

# preciso terminar ainda 

chaves ={
'suco de laranja':120,
'morango fresco': 85,
'mamao' :85,
'goiabada vermelha': 70,
'manga':56,
'laranja':50,
'brocolis':34}

n = int(input())


for i in range(n):
    qtde, fruta = input().split()



    total = qtde * fruta
    

if total > 130:
    print(f'Menos {total-130} mg')
elif total < 110:
    print(f'Mais {total} mg')
else:
    print(f'{total} mg')

















