# CLASE PRESENTADA POR DARIO TAMINI

package test;

import domain.Persona;

public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int [3] [2];
        System.out.println("edades = " + edades);
        edades [0][0] = 5; // llenado manual
        edades[0][1] = 7; // es una diferente columna
        edades[1][0] = 8;
        edades[1][1] = 4;
        edades[2][0] = 2;
        edades[2][1] = 9;    
        
        System.out.println("edades 0-0 = " + edades [0][0]);
        System.out.println("edades 0-1 = " + edades[0][1]);
        System.out.println("edades 1-0 = " + edades[1][0]);
        System.out.println("edades 1-1 = " + edades[1][1]);
        System.out.println("edades 1-1 = " + edades[2][0]);
        System.out.println("edades 1-1 = " + edades[2][1]);
        
        System.out.println("Recorremos la matriz a travez del ciclo FOR");
        for (int fila = 0; fila < edades.length; fila++){
            for (int col = 0; col < edades[fila].length; col++){
                System.out.println("edades " +fila+"-"+col+": "+edades[fila][col]);
            }
        }

# CLASE PRESENTADA POR GUSTAVO DE LLAC

class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor
    variableClase = "Esta es una variable de clase"  # este atributo está relacionado con la clase

    def __init__(self, variableInstancia):  # Variable de instancia, este atributo recibirá un valor para cada objeto
        # instanciado de esta clase
        self.variableInstancia = variableInstancia  # este atributo está relacionado con las instancias

print(MiClase.variableClase)

miClase1 = MiClase("Esta es una variable de instancia")
print(miClase1.variableInstancia)
print(miClase1.variableClase)
miClase2 = MiClase("Esta es otra variable de instancia")
print(miClase2.variableInstancia)
print(miClase2.variableClase)

# CLASE PRESENTADA POR JULIETA GUTIERREZ

class Persona:
    contador_personas = 0    # VARIABLE DE CLASE
    #vamos a agregar lo que es un metodo de clase agregamos un decorador
"""
En la linea 7 a la 10 lo que se puede hacer atraves de este metodo de clases es: Podemos incrementar valores sin crear un objeto 
"""

    @classmethod  # de la linea 8 a la 16 es contexto estetico
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self,nombre ,edad):   # contexto dinamico
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad



persona1 = Persona('Ariel',40)
print(persona1)
persona2 = Persona('Osvaldo',45)
print(persona2)
persona3 = Persona('Liliana',35)
print(persona3)
Persona.generar_siguiente_valor()# Para acceder aun metodo de clase,como a una variable de clase  vamos a necesitar hacerlo desde la misma clase
persona4 = Persona('Natalia',35)        #vamos a crear otro objeto
print(persona4)

print(f'Valor contador Persona: {Persona.contador_personas}')


#CLASE PRESENTADA POR LEONEL REAL
from abc import ABC, abstractmethod


# ABC significa: Abstract Base Class, convierte una clase en abstracta

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo para el ancho: {ancho}')
        if self._validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo para el alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f'valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f'valor erroneo alto: {alto}')

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'

    def _validar_valores(self, valor): # Método encapsulado
        return True if 0 < valor < 10 else False

# CLASE PRESENTADA POR BELÉN RABEL

class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor de clase'
    variable_clase = 'Esta es una variable'

    def __init__(self, variable_instancia):  # La variable de instancia, da diferentes valores
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():  # Método estático, se asocia a la clase
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.MiClase.variable_clase)


print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

MiClase.variable_clase2 = 'valor de la variable de clase 2'
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

MiClase.metodo_estatico()

MiClase.metodo_clase()

#CLASE PRESENTADA POR NICOLAS ABETE

class Persona:
    def __init__(self,nombre, edad):
        self.nombre= nombre
        self.edad= edad 
def __add__ (self, other): # Other significa otro
 return f'{self.nombre} {other.nombre}'

def __sub__(self, otro): # Sub significa = substraction (resta)
 return self.edad- otro.edad
Personal Persona('Ariel', 40)
persona2= Persona('Betancud', 5)
# personal. __add_(persona2) sintaxis interna y automatica

print (personal + persona2)
print (personal - persona2)
        
        #Clase Presentada por Gaston Riveros
        class Vehiculo:
## Crear un objeto de cada Clase

    def __init__(self, color, ruedas):
        self.color =color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color :' + self.color+', Ruedas'+ str(self.ruedas)
class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __int__(self):
        return super().__str__()+', Velocidad(km/hr): ' + str(self.velocidad)

    class Bicicicleta(Vehiculo):
        def __int__(self, color, ruedas, tipo):
            super().__init__(color, ruedas)
            self.tipo = tipo

        def __str__(self):
            return super().__str__()+' Tipo: '+ self.tipo

    # Primer objeto de la clase padre Vehiculo
    vehiculo = Vehiculo('Blanco', 4)
    print(vehiculo)

    # Segundo Objeto, pero ahora de la clase Auto
    auto= Auto( 'Amarillo', 4, 120)
    print(auto)

    # Tercer objeto, el ultimo de la clase Bicicleta
    bici = Bicicicleta('Azul', 2, 'Urbana')
    print(bici)
