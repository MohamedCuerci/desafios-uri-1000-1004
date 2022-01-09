

n = int(input())

matriculas = []
maioresNota = []

for i in range(n):
    matricula, nota = input().split()
    nota = float(nota)
    matricula = int(matricula)

    if nota >= 8:
        matriculas.append(matricula)
        maioresNota.append(nota)

aux = 0
pos = 0

for x in matriculas:
  if x > aux:
    aux = x
    pos = x

if pos == 0:
  print("Minimum note not reached")

else:
  print(pos)    