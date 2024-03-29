
class Pila:
    def __init__(self):
        self.items=[]
    def apilar(self,x):
        self.items.append(x)
    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")
    def es_vacia(self):
        return self.items == []


def calculador_polaca(elementos):
    p = Pila()
    for elemento in elementos:
        print("Debug:", elemento)
        try:
            numero = float(elemento)
            p.apilar(numero)
            print("DEBUG: apila",numero)
        except ValueError:
            if elemento not in "+ - * / %" or len(elemento) != 1:
                raise  ValueError("Operando invalido")
            try:
                a1 = p.desapilar()
                print("DEBUG: desapila ",a1)
                a2 = p.desapilar()
                print("DEBUG: desapila ",a2)
            except ValueError:
                print("DEBUG: error pila faltan operandos")
                raise ValueError("Faltan operandos")
            if elemento == "+":
                resultado = a2 + a1
            elif elemento =="-":
                resultado = a2 - a1
            elif elemento =="*":
                resultado = a2 * a1
            elif elemento =="/":
                resultado = a2 / a1
            elif elemento =="%":
                resultado = a2 % a1
            print("DEBUG: apila ", resultado)
            p.apilar(resultado)
    res = p.desapilar()
    if p.es_vacia():
        return res
    else:
        print("DEBUG: error pila sobran operandos")
        raise ValueError("Sobran operandos")
def main():
    expresion = input("Ingrese la expresion a evaluar: ")
    elementos = expresion.split()
    print(calculador_polaca(elementos))
main()


