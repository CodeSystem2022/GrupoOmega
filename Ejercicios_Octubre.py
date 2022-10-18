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

# EJERCICIO PRESENTADO POR LEONEL REAL

class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es documentación de la clase en Python
    Vamos a hacer en esta clase algunas operaciones de: suma, resta, multipliciación y más
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Método para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7, 9)  # Le pasamos los argumentos para los operadores
print(f'La suma de los números es: {aritmetica1.sumar()}')
print(f'La resta de los números es: {aritmetica1.resta()}')
print(f'La multiplicación de los números es: {aritmetica1.multiplicar()}')
print(f'La division de los números es: {aritmetica1.dividir():.2f}')

# Tarea realizada Julieta Gutierrez

class Cubo:
    """
    Crear la clase Cubo con los atributos,ancho,alto,y profundidad ,con
    un método calcular_volumen que tendra la formula:
    volumen= ancho * altura * profundidad
    que el usuario ingrese los valores
    """
    def __init__(self,ancho,alto,profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad
    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

ancho = int(input('Digite el ancho del cubo: '))
alto = int(input('Digite el alto para el cubo: '))
profundidad = int(input('Digite a profundidad del cubo: '))

cubo1 = Cubo(ancho,alto,profundidad)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()}') # Al llamar al objeto cubo1 al método calcular_volumen

#Ejercisio precentado por Nicolas Abete


#Como hacer la igualdad de dos conjuntos
print(conjunto1 | conjunto2)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))# acá preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.isssubperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

#Clase presentada por Gaston Riveros
persona1= Persona("Gaston","Riveros",32) #NECESITAMOS ENVIAR ARGUMENTOS
# print(persona1.nombre) # Tarea: Hacer el print igual que con el objeto 2
#Print( persona1.apellido)
# print(persona1.edad)
print(f"El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")
persona2= Persona("Pepe","Juarez", 35)
print(f"Elobjeto2 de la clase persona: {persona2.nomre} {persona2.apellido} {persona2.edad}"

      #Los atributos son: caracteristicas
# los metodos son : el comportamiento que van a tener los objetos(acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()
