class For:
    def __init__(self):
        pass

    def usoFor(self):
        nombre= "Daniel"
        datos=["Daniel",58,True]
        numeros= (2,5.6,4,1)
        docente= {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        listanotas= [(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        acum=0
        cont=0
        for notas in listanotas:
            print("primer for",notas)
            acumparcial=0
            contparcial=0
            
            for nota in notas:
                acumparcial+=nota
                contparcial+=1
                acum=acum+nota
                cont=cont+1
                print(acumparcial/contparcial)
            print(acum/cont) 

        

bucle = For()
bucle.usoFor()