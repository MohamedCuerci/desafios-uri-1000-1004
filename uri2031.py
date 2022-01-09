

n = int(input())

for i in range(n):
    jogador1 = input()
    jogador2 = input()
    
    if jogador1 == 'ataque' and jogador2 == 'pedra':
        print(f'Jogador 1 venceu')
    if jogador1 == 'pedra' and jogador2 == 'papel':
        print('Jogador 1 venceu')
    if jogador1 == 'papel' and jogador2 == 'ataque':
        print('Jogador 2 venceu')
    if jogador1 == 'papel' and jogador2 == 'papel':
        print('Ambos venceram')
    if jogador1 == 'pedra' and jogador2 == 'pedra':
        print('Sem ganhador')
    if jogador1 == 'ataque' and jogador2 == 'ataque':
        print('Aniquilacao mutua')
    if jogador2 == 'ataque' and jogador1 == 'pedra':
        print(f'Jogador 2 venceu')
    if jogador2 == 'pedra' and jogador1 == 'papel':
        print('Jogador 2 venceu')
    if jogador2 == 'papel' and jogador1 == 'ataque':
        print('Jogador 1 venceu')
    
    
