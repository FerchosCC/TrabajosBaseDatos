#index
print("index")
versiones_plone = [2.1,2.5,3.6,4,5,6,4]
print(versiones_plone.index(4),"\n")


print(versiones_plone.index(4,2))#4 = numero que busco, 2 casilla en la que empiezo a buscar
print(versiones_plone.index(4,5))
print(versiones_plone.index(6,2))
print(versiones_plone.index(3.6,3))

print(versiones_plone.index(9))

#insert
print("\n INSERT")
versiones_plone = [2.1,2.5,3.6,4,5,6]
print(versiones_plone)
versiones_plone.insert(2,3.7)#2 = pocicion en la que se va a poner el dato, 3.7 = valor que se va a agregar
print(versiones_plone)

