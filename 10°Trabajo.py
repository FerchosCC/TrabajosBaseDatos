c = 1
Comida = ["Carnita","Torta","Milanesa","Enfrijolafa","Sopa"]
Bebida = ["Pepsi","Boiing","Coca","Manzanita","Fanta"]
Alumno = []
Comida.append("Carnita")
while c == 1:
    Opcion = int(input("Que decea hacer?\n  1-Agregar Alumno\n  2-Generar Pedido\n  3-Imprimir todo\n  4-Sair\n"))
    if Opcion == 1:
        nombre = input("Cual es el nombre del alumno?: ")
        Alumno.append(nombre)

    if Opcion == 2:
        for alumno,comida,bebida in zip(Alumno,Comida,Bebida):
            print("Al alumno {0} se le dio una {1} y una {2}".format(alumno,comida,bebida))
        Alumno.reverse()
        for i in range(len(Alumno)):
            Alumno.pop()
        print(Alumno)

    if Opcion == 3:
        print(f"Hay de comer:{Comida}\n Hay de beber: {Bebida}\n Estan en fila {len(Alumno)} alumnos: {Alumno}")

    if Opcion == 4:
        C = 2
