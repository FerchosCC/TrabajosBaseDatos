class Pila:
    def __init__(self):
        self.items=[]
    def apilar(self,x):
        self.items.append(x)
    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")
    def es_vacia(self):
        return self.items == []

    def imprimir_Pila(self):
        for item in self.items:
             print(str(item))
p = Pila()
c = 1
while c == 1:
    Opcion = int(input("Que desea hacer?\n  1.Agregar\n  2.Eliminar\n  3.Saber si esta lleno\n  4.Ver pila\n  5.Salir"))
    if Opcion == 1:
        valor = input("Ingrese lo qe quiere agregar:  ")
        p.apilar(valor)
    if Opcion == 2:
        print("Se elimino: ",p.desapilar())
    if Opcion == 3:
        if p.es_vacia() == True:
            print("La pila esta vacia")
        else:
            print("La pila tiene elementos")



