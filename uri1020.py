ano = int(input())

a = ano // 365
n = ano - a*365

m = n // 30
n = n - m*30

d = n

print(f'{a} ano(s)')
print(f'{m} mes(es)')
print(f'{d} dia(s)')