i = 0
j = 1
while(i<=2):
    if(i==2.0 or i ==1.0):
        print(f'I={i:.0f} J={j+i:.0f}')
        print(f'I={i:.0f} J={j+1+i:.0f}')
        print(f'I={i:.0f} J={j+2+i:.0f}')
        i = i + 0.2
    else:
        print(f'I={i} J={j + i}')
        print(f'I={i} J={j + 1 + i}')
        print(f'I={i} J={j + 2 + i}')
        i = round(i + 0.2,2)

