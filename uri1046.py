# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, 
# sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora 
# e máxima de 24 horas.

# hi = hora inicial 
# hf = hora final

hi, hf = input('').split()

hi = int(hi)
hf = int(hf)

if hi < hf:
    ht = hf - hi
else:
    ht = (24-hi) + hf
# saida

print(f'O JOGO DUROU {ht} HORA(S)')





