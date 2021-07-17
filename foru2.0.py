class For:
    def __init__(self):
        pass

    def usoFor(self):
        nombre= "Daniel"
        datos=["Daniel",58,True]
        numeros= (2,5.6,4,1)
        docente= {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        listanotas= [(30,40),(20,40),(50,40)]
        listaAlumnos= [{"nombre": "Erick","edad":20, "final": "70"}, {"nombre": "Yadi", "final" :60 }]
        print("\nDiccionario de alumnos")
        print(listaAlumnos)
        acum=0

        for alumnos in listaAlumnos:
            print(alumnos,len(alumnos))

        for clave,valor in alumnos.items():
                print(clave,":",valor,end=" ")
                if clave == 'final':
                    acum=acum+valor

                print()
        print("Promedio",acum/len(listaAlumnos))
            


bucle = For()
bucle.usoFor()