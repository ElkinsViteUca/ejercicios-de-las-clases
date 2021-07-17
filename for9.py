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
        for notas in listanotas:
            print("for externo",notas,end="")
            for nota in notas:
                print(nota,end="")
            print("Saliendo del for interno")


bucle = For()
bucle.usoFor()