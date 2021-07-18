class Ordenar:
    def __init__(self,lista):
        self.lista=lista

    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
    
    def recorrerPosicion(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)

    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos)

lista =[2,3,1,5,8,10]
ord1 = Ordenar(lista)
ord1.recorrerRange()