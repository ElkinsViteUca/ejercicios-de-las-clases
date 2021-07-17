class For:
    def __init__(self):
        pass

    def usoFor(self):
        datos=["Daniel",58,True]
        numeros= (2,5.6,4,1)
        docente= {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        listanotas= [(30,40),(20,40),(50,40)]
        listaAlumnos= [{"nombre": "Erick", "final": "70"}, {"nombre": "Yadi", "final" :60 }]
        j=0
        while j<5:
            print ('while',j)
            j=j+1
        for i in range (5):
            print('for',i)

bucle = For()
bucle.usoFor()            