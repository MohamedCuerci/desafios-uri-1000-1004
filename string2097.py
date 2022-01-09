
# esquece isso kkkk

def unidade(n):
    if len(n) == 1:
            if n == '0':
                return 'zero'
            elif n == '1':
                return 'um'
            elif n == '2':
                return 'dois'
            elif n == '3':
                return 'tres'
            elif n == '4':
                return 'zero'
            elif n == '5':
                return 'zero'
            elif n == '6':
                return 'zero'
            elif n == '7':
                return 'zero'
            elif n == '8':
                return 'zero'
            elif n == '9':
                return 'zero'
            
def dezena(n):
    if n == '1':
        pass

def centena(n):
    if n == '100':
        return 'cem'
    elif n[0] == '1':
        return 'cento'
    elif n[0] == '2':
        return 'duzentos' 
    elif n[0] == '3':
        return 'trezentos' 
    elif n[0] == '4':
        return 'quatrocentos' 
    elif n[0] == '5':
        return 'quinhentos' 
    elif n[0] == '6':
        return 'seiscentos' 
    elif n[0] == '7':
        return 'setecentos' 
    elif n[0] == '8':
        return 'oitocentos' 
    elif n[0] == '9':
        return 'novecentos' 

def milhares(n):
    if n == '1000':
        return 'mil'
    elif n == '2':
        return 'dois mil' 
    elif n == '3':
        return 'tres mil' 
    elif n == '4':
        return 'quatro mil' 
    elif n == '5':
        return 'cinco mil' 
    elif n == '6':
        return 'seis mil' 
    elif n == '7':
        return 'sete mil' 
    elif n == '8':
        return 'oito mil' 
    elif n == '9':
        return 'nove mil' 


while True:
    try:
        n = input()

        

    except:
        break