

while True:
    try:
        bacteria1 = 'GCTTTCGACGAT'
        bacteria2 = 'GATCGAGCTTCGAA'
        bacteria3 = 'GGTCTAGCTAAT'
        cura = 'TCGA'

        if cura in bacteria1:
            bacteria1 -= cura
            print(bacteria1)
        """ else:
            print('Nao resistente') """
       
    except EOFError:
        break











