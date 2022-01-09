
notaTotal = 0 
cont = 0
continuar = True



while continuar==True:
  nota = float(input())
  
  if nota>=0 and nota <=10:
    notaTotal += nota
    cont += 1 

    if cont == 2:
      print("media = %.2f"%(notaTotal/2))
      cont = 0 
      notaTotal = 0

      while True:
        print("novo calculo (1-sim 2-nao)")
        pergunta = int(input())
        if pergunta == 2:
          continuar = False
          break
        elif pergunta == 1:
          continuar = True
          break
      
  else:
    print("nota invalida")