#Bucle
#Para hacer que funcione solo quita el gato de abajo
def imprimir(x):
    print(x)
    imprimir(x-1)
#imprimir(0)

def imprimir2(x):
    if x>0:
        print(x)
        imprimir2(x-1)
#imprimir2(5)

def imprimir3(x):
    if x>0:
        imprimir3(x-1)
        print(x)
#imprimir3(5)

def factorial(fact):
    if fact>0:
        valor = fact*factorial(fact-1)
        return valor
    else:
        return 1
#print(f"El factorial de 4 es {factorial(4)}")

def ordenar(lista,cant):
    if cant>1:
        for f in range(0, cant-1):
            if lista[f]>lista[f+1]:
                aux = lista[f]
                lista[f] = lista[f+1]
                lista[f+1] = aux
            ordenar(lista,cant-1)
datos=[60,44,22,33,2]
print(datos)
ordenar(datos,len(datos))
print(datos)