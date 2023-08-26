c = 1  #Condicion para el ciclo while
A = [] #Arreglo que guarda todos los datos
B = [] #Arreglo que cuenta las carreras elegidas

class Alumno:
    Nombre = ""
    Carrera = ""
    Semestre = 0
    RFC = ""
    NoControl = 0

    def __init__(self, Nombre, Carrera, Semestre, RFC, NoControl):
        self.Nombre = Nombre
        self.Carrera = Carrera
        self.Semestre = Semestre
        self.RFC = RFC
        self.NoControl = NoControl

    def elegirCarrera(self,Eleccion):
        if Eleccion == 1:
            self.Carrera = "TIC´S"
        if Eleccion == 2:
            self.Carrera = "Sistemas"
        if Eleccion == 3:
            self.Carrera = "Industrial"
        if Eleccion == 4:
            self.Carrera = "Electromecanica"
        if Eleccion == 5:
            self.Carrera = "Gestion empresarial"
    def imprimir(self):
        print(self.Nombre)
        print(self.Carrera)
        print(self.Semestre)
        print(self.RFC)
        print(self.NoControl)


def agregar_nueva_fila(array, datos_fila):
    nueva_fila = datos_fila
    array.append(nueva_fila)



while c == 1:
    Opcion = int(input("Que decea hacecr?:\n  1-Agregar Alumno\n  2-Mostrar Todos los alumnos\n"
                   "  3-Buscar por Carrera\n  4-Buscar por Alumno\n  5-Cuantos Alumnos hay\n  6-Salir\n  "))
    if Opcion == 1:
        nom = input("Escribe tu nombre: ")
        sem = int(input("Escribe tu semestre: "))
        rfc = input("Escribe tu RFC: ")
        control = int(input("Escribe tu numero de control: "))

        Alumno1 = Alumno(nom,"",sem,rfc,control)

        Eleccion = int(input("Que carrera decea?:\n  1-TIC´S\n  2-Sistemas\n  3-Industrial\n"
                             "  4-Electromecanica\n  5-Gestion empresarial\n  "))

        B.append(Eleccion)

        Alumno1.elegirCarrera(Eleccion)

        datos_para_fila = [Alumno1.Nombre,Alumno1.Carrera,Alumno1.Semestre,Alumno1.RFC,Alumno1.NoControl]
        agregar_nueva_fila(A, datos_para_fila)


    if Opcion == 2:
        for fila in A:
            print(fila)

    if Opcion == 3:
        print("TIC´S ->", B.count(1))
        print("Sistemas ->", B.count(2))
        print("Industrial ->", B.count(3))
        print("Electromecanica ->", B.count(4))
        print("Gestion Empresarial ->", B.count(5),"\n")

    if Opcion == 4:
        palabra_buscar = input("Ingrese el nombre del alumno : ")
        contador = 0
        for palabra, _,_,_,_ in A:
            if palabra == palabra_buscar:
                contador += 1
        print(f"El nombre '{palabra_buscar}' se repite {contador} veces.\n")
    if Opcion == 5:
        print(f"Hay {len(A)} registrados")

    if Opcion == 6:
        c = 2