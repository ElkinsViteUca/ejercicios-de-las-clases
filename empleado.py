
from cargo import cargo


class Empleado:
    secuencia = 0
    def __init__(self,cod=99,nom="",sue="",car=None):
        self.codigo=self.generaCodigo()
        self.nombre=nom
        self.sueldo=sue
        self.cargoEmp=car

    def generaCodigo(self):
            Empleado.secuencia=Empleado.secuencia+1
            return Empleado.secuencia   

    def mostrar(self):
            print("codigo:{} Nombre:{} cargo({}):{}".format(self.codigo,self.nombre,self.cargoEmp.codigo,self.cargoEmp.descripcion))        

cargo1=cargo("Docente")
emp1=Empleado("Daniel",1000,cargo1)
emp1.mostrar()