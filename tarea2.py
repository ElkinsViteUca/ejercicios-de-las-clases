class Tarea:
    def __init__(self):
        pass
    def factorial(self):
        n=int(input("Ingrese numero: "))
        for i in range (n):
            numero=int(input("Ingrese numero:"))
            acu=1
            for num in range(numero,1,-1):
                acu = acu*num
            print("numero: {} factorial={}".format(numero,acu))

tarea = Tarea()
tarea.factorial()


    