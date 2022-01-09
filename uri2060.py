
n = int(input())

m2 = 0
m3 = 0
m4 = 0
m5 = 0

x = input('tropa: ').split()

for i in range(n):
    if int(x[i]) % 2 == 0:
        m2 += 1
    if int(x[i]) % 3 == 0:
        m3 += 1
    if int(x[i]) % 4 == 0:
        m4 += 1
    if int(x[i]) % 5  == 0:
        m5 += 1


print(f'{m2} multiplo(s) de 2')
print(f'{m3} multiplo(s) de 3')
print(f'{m4} multiplo(s) de 4')
print(f'{m5} multiplo(s) de 5')