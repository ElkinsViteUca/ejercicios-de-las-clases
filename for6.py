class For:
    def __init__(self):
        pass

    def usoFor(self):
        nombre= "Daniel"
        datos=["Daniel",58,True]
        numeros= (2,5.6,4,1)
        docente= {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        listanotas= [(30,40),(20,40),(50,40)]
        listaAlumnos= [{"nombre": "Erick", "final": "70"}, {"nombre": "Yadi", "final" :60 }]
        # for i in range (5):
        #     print('for',i,end="")
        # print()
        # for i in range (1,5):
        #     print('for',i,end="")
        # print()
        # for i in range (2,10,2):
        #     print('for',i,end="")
        # print()
        # for i in range (12,3,-3):
        #     print('for',i,end="")
        
        for elem in nombre:
            print (elem,end="")

bucle = For()
bucle.usoFor()