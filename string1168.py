n = int(input('dale: '))

for y in range(n):
    led = 0
    x = input('numeros: ')
    for i in range(len(x)):
        if x[i] == '1':
            led = led + 2
        if x[i] == '2':
            led = led + 5
        if x[i] == '3':
            led = led + 5
        if x[i] == '4':
            led = led + 4
        if x[i] == '5':
            led = led + 5
        if x[i] == '6':
            led = led + 6
        if x[i] == '7':
            led = led + 3
        if x[i] == '8':
            led = led + 7
        if x[i] == '9':
            led = led + 6
        if x[i] == '0':
            led = led + 6
    print(f'{led}')
