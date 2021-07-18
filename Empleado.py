from cargo3 import Cargo
class Empleado:
    secuencia=0
    def __init__(self,cod=99,nom="",sue="",car=None):
        Empleado.secuancia=Empleado.secuencia+1
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.sueldo=sue
        self.cargo=car

    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia

    def mostrar(self):
        print("Codigo: {} Nombre:{} Cargo({}):".format(self.codigo,self.nombre,self.cargo.cargo,self.cargo.descripcion))

cargo1=Cargo("Docente")
emp1 = Empleado("Daniel",1000,cargo1)
emp1.mostrar()
emp2 = Empleado("Moises",1000,cargo1)
emp2.mostrar()
