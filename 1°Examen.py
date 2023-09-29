
class llenado:
    def __init__(self):
        self.Contador = 0
        self.Contador2 = 0
        self.Contador3 = 0
        self.N1 = 0
        self.N2 = 13
        self.x = 0
        self.y = 0
        self.c = 0
    def derecha(self):
        if self.Contador <= 3:
            Arreglo = []
            for i in range(3):
                self.N1 = self.N1 + 1
                Arreglo.append(self.N1)
            print(Arreglo)
            self.Contador += 1
            self.derecha()
    def izquierda(self):
        if self.Contador2 <= 3:
            Arreglo = []
            for i in range(3):
                self.N2 = self.N2 - 1
                Arreglo.append(self.N2)
            print(Arreglo)
            self.Contador2 += 1
            self.izquierda()
    def abstracto(self):
        if self.x == 0:



Ejemplo1 = llenado()
#Ejemplo1.derecha()
#Ejemplo1.izquierda()
Ejemplo1.abstracto()
