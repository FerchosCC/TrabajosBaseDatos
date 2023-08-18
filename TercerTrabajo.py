A = []
n = 1
c = 0
while n == 1:
    A.append(0)
    nombre = input("Escribe tu nombre: ")
    Edad = input("Escribe tu Edad: ")
    A[c] = nombre,Edad
    c = c + 1
    print(A)
    n = int(input("Quiere agregar otro usuario?:\n  1.Si\n  2.No\n   "))
print(f"Agrego {c} usuarios")



