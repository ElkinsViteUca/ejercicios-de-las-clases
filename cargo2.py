class Cargo:
    def __init__(self,des,cod):
        self.codigo=cod
        self.descripcion=des

cargo1 = Cargo()
print(cargo1.codigo,cargo1.descripcion)
cargo2 =Cargo()
cargo2.codigo=1
cargo2.descripcion=(100,"Docente")
print(cargo2.codigo,cargo2.descripcion)
cargo3=Cargo(101)
cargo3.descripcion="Conserje"
print(cargo3.codigo,cargo3.descripcion)