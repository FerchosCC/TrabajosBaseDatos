Factura=["pan","huevos",100,1234]
print(Factura,"\n")

print(Factura[0])
print(Factura[3],"\n")

print(Factura[-1])
print(Factura[-2])
print(Factura[-3])
print(Factura[-4],"\n")

print(len(Factura))
print(len(Factura)-1)
print(Factura[-len(Factura)],"\n")

Factura[1]="Carne"
print(Factura,"\n")

factura=["pan","carne",100,1234]
electronica=["telefono",500]
factura[2]=electronica
print(factura)
