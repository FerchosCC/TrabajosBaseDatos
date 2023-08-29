#pop
print("POP")
versiones_plone = [2.1,2.5,3.6,4,5,6]
print(versiones_plone.pop())
print(versiones_plone)


print(versiones_plone.pop(2))# 2 = pocicion
print(versiones_plone)

#Remove
print("\nREMOVE")
versiones_plone = [2.1,2.5,3.6,4,5,6]
print(versiones_plone)
versiones_plone.remove(2.5)
print(versiones_plone)

#reverse
print("\nREVERSE")
versiones_plone = [2.1,2.5,3.6,4,5,6]
print(versiones_plone)
versiones_plone.reverse()
print(versiones_plone)

#sort
print("\nSORT")
versiones_plone = [4,2.5,5,3.6,2.1,6]#El arreglo debe estar compuesto de puros numeros o de puras letras
print(versiones_plone)
versiones_plone.sort()
print(versiones_plone)

versiones_plone.sort(reverse=True)
print(versiones_plone)

#comvertir a listas
print("\ncovertir a listas")

vocales = "aeiou"
for letra in "Hermosa":
    if letra in vocales:
        print(letra)

#Split
print("\nSPLIT")
mensaje = "Hola, como estas tu?"
mensaje.split()
for palabra in mensaje.split():
    print(palabra)
#PREGUNTAS
print("\nPREGUNTAS")
preguntas = ["nombre","objetivo","sistema operativo"]
respuestas = ["Leonardo","Aprender python y plone","linux"]
for pregunta, respuesta in zip(preguntas,respuestas):
    print("Cual es tu {0}?, la respuesta es: {1}.".format(pregunta,respuesta))
