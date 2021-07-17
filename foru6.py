class For:
    def __init__(self):
        pass

    def usoFor(self):
        nombre= "Daniel"
        datos=["Daniel",58,True]
        numeros= (2,5.6,4,1)
        docente= {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        listanotas= [(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        acum,cont=0,0
        for notas in listanotas:
            print(notas)
            acumparcial=0
            for nota in notas:
                acumparcial +=nota
            cont=cont+1
            acum=acum+acumparcial
            print("TotalParcial:{} PromParcial:{}".format(acumparcial,acumparcial/len(notas))
        print("TotalParcial:{} PromParcial:{}".format(acum,acum/cont))
bucle = For()
bucle.usoFor()