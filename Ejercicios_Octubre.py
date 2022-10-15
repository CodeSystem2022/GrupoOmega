# CLASE PRESENTADA POR DARIO TAMINI

class Rectangulo:
    '''
    crear una clase llamada rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular area utilizando la formula:
    area = base * altura
    pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser 3
    '''

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura


base = int(input("Digite el numero para la base del rectangulo: "))
altura = int(input("Digite el numero para la altura del rectangulo: "))
rectangulo1 = Rectangulo(base, altura)
print(f"El area del rectangulo es: {rectangulo1.calcular_area()}")


# EJERCICIO PRESENTADO POR GUSTAVO DE LLAC

"""
Crear clase Cubo con los atributos: ancho, alto y profundidad.
Con un método calcular_volumen que tendrá la formula:
volumen = ancho * altura * profundidad.
El usuario debe ingresar los valores
"""
class Cubo:
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

print(">>>>Cálculo volumen de un cubo<<<<")
ancho = float(input("Digite ancho del cubo: "))
altura = float(input("Digite altura del cubo: "))
profundidad = float(input("Digite profundidad del cubo: "))
cubo1 = Cubo(ancho, altura, profundidad)
print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")
