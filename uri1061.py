

fodase, diaInicial = input().split()
diaInicial = int(diaInicial)

horai, minutoi, segundoi = input().split(':')

horai = int(horai)
minutoi = int(minutoi)
segundoi = int(segundoi)

###########################################################

fodase1 , diaFinal = input().split()
diaFinal = int(diaFinal)

horaf, minutof, segundof = input().split(':')

horaf = int(horaf)
minutof = int(minutof)
segundof = int(segundof)

#########################################################

if diaFinal >= diaInicial:
    diaTotal = diaFinal - diaInicial 

if horaf > horai:
    horatotal = horaf - horai
else:
    horatotal = (24-horai) + horaf
    diaTotal -= 1

if minutof >= minutoi:
    minutoTotal = minutof - minutoi
else:
    minutoTotal = (60-minutoi) + minutof

if segundof >= segundoi:
    segundoTotal = segundof - segundoi
else:
    segundoTotal = (60-segundoi) + segundof


###############################################

print(f'{diaTotal} dia(s)')
print(f'{horatotal} hora(s)')
print(f'{minutoTotal} minuto(s)')
print(f'{segundoTotal} segundo(s)')











