class Cargo:
    def __init__(self,des="Sin Cargo"):
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia
        self.descripcion=des

cargo1 = Cargo()
print(cargo1.codigo,cargo1.descripcion)
cargo2 =Cargo(100,"Docente")
print(cargo2.codigo,cargo2.descripcion)
cargo3=Cargo()
print("cargo3",cargo3.codigo,cargo3.descripcion)
print(Cargo.secuencia)