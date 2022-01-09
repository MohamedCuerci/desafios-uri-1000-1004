
while True:
    try:
        n1 = float(input())
        n2 = float(input())

        n1 = str(n1)
        n2 = str(n2)
        
        n1 = n1.split('.')
        n2 = n2.split('.')

        n1decimal = n1[1]
        n2decimal = n2[1]    

        if float(n1decimal) > float(n2decimal):
            n0 = n1[0]
            n0 = int(n0)
            print(n0+1)
        else:
            n0 = n1[0]
            n0 = int(n0)
            if n0 == 0:
                print(1)
            else:
                print(n0)

    except EOFError:
        break



















