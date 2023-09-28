class Cafeteria: #Creo una clase
    def __init__(self,Comida,Bebida): #En estos dos espacios voy a guardar 2 arreglos uno de comida y otro de bebida
        self.Comida = Comida
        self.Bebida = Bebida
        self.Ordenes = [] #Arreglo que guarda las ordenes que le llegan
        self.Contcom = [] #Arreglo que guarda la comida que se pidio en forma numerica 1 = milanesa, 2=Pollo ...
        self.Contbeb = [] #Arreglo que guarda las bebidas que se pidieron en forma numerica, 1= Fanta, 2=CocaCola ...

    def Menu(self): #Menu que se llama a si mismo
        Opcion = int(input("Que desea hacer?:\n  1-Pedir\n  2-Cancelar Pedido\n  3-Ver menu\n  "
                           "4-Ver Ordenes\n  5-Servir Ordenes\n  6-Salir\n"))
        if Opcion == 1:
            self.Pedir()
        if Opcion == 2:
            self.CancelarPedido()
        if Opcion == 3:
            self.VerMenu()
        if Opcion == 4:
            self.VerOrdenes()
        if Opcion == 5:
            print("Todas las ordenes han sido despachadas")
            self.Ordenes = []
        if Opcion < 6:
            self.Menu() #Aqui se llama a si mismo

    def Pedir(self):
        com = int(input(f"Elija un Alimento\n  1-{self.Comida[0]}\n  2-{self.Comida[1]}\n  3-{self.Comida[2]}\n"))
        beb = int(input(f"Elija una Bebida\n  1-{self.Bebida[0]}\n  2-{self.Bebida[1]}\n  3-{self.Bebida[2]}\n"))
        self.Contcom.append(com-1) #Se guarda la opcion tomada en el arrgelo de comida pedida Contcom
        self.Contbeb.append(beb-1) #Se guarda la opcion tomada en el arreglo de bebida pedida Contbeb
        pedido = [self.Comida[com - 1], self.Bebida[beb - 1]] #Lass opciones se guardan en el pedido
        print(pedido)
        self.Ordenes.append(pedido)#Para previamente guardar el pedido en las ordenes

    def VerOrdenes(self):
        op = int(input("Como desea ver las ordenes?\n  1-Ver contador\n"
                       "  2-Ordenar conforme al abecedario\n  3-Ver original"))
        if op == 1:
            for i in range(3):
                print(f"{self.Comida[i]} --> {self.Contcom.count(i)}")#Aqui te dice cuantas veces se pidio cada cosa
                print(f"{self.Bebida[i]} --> {self.Contbeb.count(i)}")
        if op == 2:
            self.ordenar(self.Ordenes,len(self.Ordenes))#Aqui se ordena el arreglo Ordenes conforme al abecedario
            print(self.Ordenes)
        if op == 3:
            print(self.Ordenes) #Aqui se muestra el Arreglo original


    def CancelarPedido(self):
        self.Ordenes.pop()#Se eliminan los ultimos 2 pedidos
        self.Contcom.pop()
        self.Contbeb.pop()

    def VerMenu(self):
        print(self.Comida) #Se muestra el menu de cocmida y bebida
        print(self.Bebida)

    def ordenar(self,lista, cant):
        if cant > 1:# Codigo para ordenr los valores de los arreglos
            for f in range(0, cant - 1):
                if lista[f] > lista[f + 1]:
                    aux = lista[f]
                    lista[f] = lista[f + 1]
                    lista[f + 1] = aux
                self.ordenar(lista, cant - 1)

comida =["Milanesa","Pollo","Lechuga"]#Solo acepta 3 valores
bebida =["Fanta","CocaCola","Pepsi"]
Prueba = Cafeteria(comida,bebida)
Prueba.Menu()# Se inicia