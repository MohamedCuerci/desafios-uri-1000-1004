
n = int(input())

for i in range(n):
    bonus = int(input())
    ataque1, defesa1, level1 = input().split()
    ataque2, defesa2, level2 = input().split()


    if int(level1) % 2 == 0:
        valor_golpe1 = ((int(ataque1) + int(defesa1)) / 2) + bonus
    else:
        valor_golpe1 = ((int(ataque1) + int(defesa1)) / 2)

    if int(level2) % 2 == 0:
        valor_golpe2 = ((int(ataque2) + int(defesa2)) / 2) + bonus
    else:
        valor_golpe2 = ((int(ataque2) + int(defesa2)) / 2)

    if valor_golpe1 > valor_golpe2:
        print('Dabirel')
    elif valor_golpe2 > valor_golpe1:
        print('Guarte')
    else:
        print('Empate')