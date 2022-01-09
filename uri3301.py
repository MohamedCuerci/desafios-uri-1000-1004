
# da algum erro que eu não entendo

huguinho  = 1
zezinho = 1
luisinho = 1

while True:
    if huguinho <= 0 and zezinho <= 0 and luisinho <= 0:
        break
    
    h, z, l = input('').split()

    h = int(h)
    z = int(z)
    l = int(l)

    if z == 6:
        print('zezinho')
        zezinho -= 1
    elif z == 5:
        print('luisinho')
        luisinho -= 1
    else:
        print('huguinho')
        huguinho -= 1