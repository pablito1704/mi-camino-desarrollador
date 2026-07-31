#Herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    pass

perro = Perro("Max")
print(perro.nombre)

#Mini Reto 1
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Gato(Animal):
    pass

gato = Gato("Michi")
print(gato.nombre)

#Ejericio 1
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Moto(Vehiculo):
    pass

moto = Moto("Yamaha")
print(moto.marca)

#Mini Reto 2
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    pass

alumno = Estudiante("Pablo")
print(alumno.nombre)

#Agregar metodos a una clase hija
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):

    def ladrar(self):
        print(f"{self.nombre} dice: Guau!")

perro = Perro("Max")
perro.ladrar()

#Ejercicio 2
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Pajaro(Animal):

    def cantar(self):
        print(f"Pi, pi. Soy {self.nombre}")
pajaro = Pajaro("Piolín")
pajaro.cantar()

#Mini Reto 3
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Gato(Animal):
    def maullar(self):
        print("Miau", self.nombre)

gato = Gato("Michi")
gato.maullar()

#Sobreescribir Metodos (Override)
class Animal:
    def hablar(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print("Guau!")

perro = Perro()
perro.hablar()

#Reto final del Día 15
class Empleado:
    def trabajar(self):
        print("El empleado esta trabajando.")

class Programador(Empleado):
    def trabajar(self):
        print("El programador está escribiendo código.")

programador = Programador()
programador.trabajar()

#Mini Reto Final
class Persona:

    def saludar(self):
        print("Hola")

class Profesor(Persona):

    def saludar(self):
        print("Buenos días")

profesor = Profesor()
profesor.saludar()