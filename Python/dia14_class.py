#Class, __init__
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

persona1 = Persona("Pablo")
print(persona1.nombre)

#Mini Reto 1
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

persona = Persona("Ana")
print(persona.nombre)

#Ejercicio 1
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
mi_perro = Perro("Max")
print(mi_perro.nombre)

#Mini Reto 2
class Auto:
    def __init__(self, marca):
        self.marca = marca
carro = Auto("Toyota")
print(carro.marca)

#Metodos
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

persona = Persona("Pablo")
persona.saludar()

#Ejercicio 2
class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def maullar(self):
        print(f"Miau, soy {self.nombre}")

gato = Gato("Michi")
gato.maullar()

#Mini Reto 3
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Hola", self.nombre)

persona = Persona("Luis")
persona.hablar()

#Varios Atributos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

persona = Persona("Pablo", 21)
persona.presentarse()

#Reto final del Día 14
class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def mostrar(self):
        print(f"Mi nombre es {self.nombre} y estudio {self.carrera}.")

estudiante = Estudiante("Pablo", "Desarrollo de Software")
estudiante.mostrar()

#Mini Reto Final
class Animal:
    def __init__(self, especie):
        self.especie = especie

animal = Animal("Perro")
print(animal.especie)