
# codigo nao funciona no uri mas esta correto

while True:
    try:
        a, b = input('').split()

        if a == '0' and b == '0':
            break

        nova_dale = ''
        for i in b:
            if i == a:
                pass
            else:
                nova_dale += i

        if nova_dale == '':
            print(0)
        else:    
            print(int(nova_dale))
    except ValueError:
        pass
    