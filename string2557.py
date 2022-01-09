

while True:
    try:
        funcao = input().replace('+', '=').split('=')
        #funcao.replace('+', '=')
        
        r = funcao[0]
        l = funcao[1]
        j = funcao[2]
       
        if 'R' in funcao:
            print(f'{int(j)-int(l)}')
        if 'L' in funcao:
            print(int(r) - int(j))
        if 'J' in funcao:
            print(int(r) + int(l))

    except:
        break











