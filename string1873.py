
def define_ganhador(jogador1, jogador2):
    '''define quem é o ganhador'''
    
    if jogador1 == jogador2:
        return 'empate'
    elif jogador1 == 'tesoura':
        if jogador2 == 'papel':
            return 'rajesh'
        elif jogador2 == 'lagarto':
            return 'rajesh'
        else:
            return 'sheldon'
    elif jogador1 == 'papel':
        if jogador2 == 'pedra':
            return 'rajesh'
        elif jogador2 == 'spock':
            return 'rajesh'
        else:
            return 'sheldon'
    elif jogador1 == 'pedra':
        if jogador2 == 'lagarto':
            return 'rajesh'
        elif jogador2 == 'tesoura':
            return 'rajesh'
        else:
            return 'sheldon'
    elif jogador1 == 'lagarto':
        if jogador2 == 'spock':
            return 'rajesh'
        elif jogador2 == 'papel':
            return 'rajesh'
        else:
            return 'sheldon'
    elif jogador1 == 'spock':
        if jogador2 == 'tesoura':
            return 'rajesh'
        elif jogador2 == 'pedra':
            return 'rajesh'
        else:
            return 'sheldon'
    else:
        return 'sheldon'


n = int(input())

for i in range(n):
    rajesh, sheldon = input().split()
    x = define_ganhador(rajesh, sheldon)

    print(x)