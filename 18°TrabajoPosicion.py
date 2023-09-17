import random

A = [random.randint(1,10),random.randint(1,10),random.randint(1,10)] #Arrelo con valores aleatorios
B = [] #Arrelo que usara el jugador
ciclo = 0 #Ciclo para el juego

#Inicia el juego
while ciclo == 0:
    print(A) #Enseña los numero que se elegieron aleatoriamente
    p = 0 #Posicion de los arrelos
    x = 0 #Cantidad de numeros a los que les atino el jugador

    #Bucle donde el jugador selecciona sus 3 numeros
    for i in range(3):
        num = int(input("Escribe un numero: "))
        B.append(num)

    #Bucle donde la computadora analiza cuantos numeros salen en el arreglo cuantas veces
    for i in range(3):
        if A.count(B[p]) > 0:
            print(f"Existen {A.count(B[p])} {B[p]}")
        p +=1

    #Reinicio de las variables a 0 para poder utilizarlas otra vez
    p = 0
    x = 0

    #Bucle donde se dice a cuantos numeros les  atino en su respectivo lugar
    for i in range(3):
        if A[p] == B[p]:
            x += 1
        p += 1

    print(f"Le atinaste a {x} numeros")

    B.clear() #Limpia el arreglo para repetir el proceso y que no se salga de los 3 numeros

    #Salida 
    if x == 3:
        print("Ganaste")
        ciclo =+ 1

