x = int(input('dale: '))

string = ''
for i in range(x):
    string += 'Ho'
    if i == (x-1):
        string += '!'
    else:
        string += ' '
print(string)