class Ordenar:
    def __init__(self,lista,enc):
        self.lista=lista

    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
    
    def recorrerEnumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)

    def recorrerRange(self):
        for pos in range(len(self.lista)):
            print(pos)

    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele == buscado:
                enc=True
                break
        if enc == True:return pos
        else: return -1

lista =[2,3,1,5,8,10] 
ord1 = Ordenar(lista)
buscado=9
resp = ord1.buscar(3)

if resp !=-1: 
    print("El Numero={} se encuentra en la podsiion: ({})".format(buscado,resp,ord1.lista))
else:
    print("El numeri={} no se encuentra en la lista".format(buscado))