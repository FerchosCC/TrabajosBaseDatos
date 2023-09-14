#Recursividad
def jugar(intento=1):
    respuesta = input("De que color es una naranja ")
    if respuesta != "naranja":
        if intento < 3:
            print("\nFallaste Intentalo de nuevo")
            intento += 1
            jugar(intento)
        else:
            print("\nPerdiste")
    else:
        print("\nGanaste")
jugar()