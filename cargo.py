class Cargo:
    def __init__(self):
        self.codigo=99
        self.descripcion="Sin cargo"

cargo1 = Cargo()
print(cargo1.codigo,cargo1.descripcion)
cargo2 =Cargo()
cargo2.codigo=1
cargo2.descripcion="Docente"
print(cargo2.codigo,cargo2.descripcion)
cargo3=Cargo()
cargo3.descripcion="Conserje"
print(cargo3.codigo,cargo3.descripcion)