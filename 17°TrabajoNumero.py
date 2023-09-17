import random

class Partida:
    def __init__(self, intentos,num,nombre,errores):
        self.intentos = intentos
        self.num = num
        self.nombre = nombre
        self.errores = errores
    def ordenar(self,lista,cant):
        if cant>1:
            for f in range(0,cant-1):
                if lista[f]>lista[f+1]:
                    aux = lista[f]
                    lista[f]=lista[f+1]
                    lista[f+1] = aux
                self.ordenar(lista,cant-1)
    def juego(self):
        valor = int(input("¿Qué número crees que es?: \n"))
        if valor == self.num:
            print(f"Ganaste con {10 - self.intentos} errores.")
            self.errores = 10-self.intentos
        elif self.intentos > 1:
            if valor < self.num:
                print("El número es mayor.")
            else:
                print("El número es menor.")
            print(f"Te quedan {self.intentos - 1} intentos.")
            self.intentos -= 1
            self.juego()
        else:
            print("Perdiste")
ciclo = 0
A = []
while ciclo == 0:
    nombre = input("Escribe tu nombre: ")
    partida1 = Partida(10, random.randint(1, 1000),nombre,0)
    Opcion = int(input("Que deseas hacer:\n  1.Jugar\n  2.Ver tabla de clasificaciones\n  3.Salir\n"))
    if Opcion == 1:
        partida1.juego()
        nuevaFila = [partida1.errores,partida1.nombre,partida1.num]
        A.append(nuevaFila)
    if Opcion == 2:
        partida1.ordenar(A,len(A))
        print(A)


