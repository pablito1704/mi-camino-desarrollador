#Mini Reto 1
class Persona:

    def __init__(self, edad):
        self.__edad = edad

    def mostrar(self):
        print(self.__edad)

persona = Persona(21)
persona.mostrar()

#Ejercicio 1
class Cuenta:

    def __init__(self, saldo):
        self.__saldo = saldo

    def mostrar_saldo(self):
        print(self.__saldo)

cuenta = Cuenta(1000)
cuenta.mostrar_saldo()

#Mini reto 2
class Producto:

    def __init__(self, precio):
        self.__precio = precio

    def mostrar_precio(self):
        print(self.__precio)

producto = Producto(850)
producto.mostrar_precio()

#Modificar un atributo privado mediante un método
class Cuenta:

    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def mostrar_saldo(self):
        print(self.__saldo)

cuenta = Cuenta(500)

cuenta.depositar(200)

cuenta.mostrar_saldo()

#Ejercicio 2
class Alcancia:

    def __init__(self, dinero):
        self.__dinero = dinero

    def guardar(self, cantidad):
        self.__dinero += cantidad

    def mostrar(self):
        print(self.__dinero)

alcancia = Alcancia(100)

alcancia.guardar(50)

alcancia.mostrar()

#Mini reto 3
class Caja:
    def __init__(self, objetos):
        self.__objetos = objetos

    def agregar(self, cantidad):
        self.__objetos += cantidad

    def mostrar(self):
        print(self.__objetos)

caja = Caja(10)

caja.agregar(5)

caja.mostrar()

#Metodo set y get
class Persona:

    def __init__(self, edad):
        self.__edad = edad

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

persona = Persona(21)
print(persona.get_edad())

persona.set_edad(25)
print(persona.get_edad())

#Reto final del Día 16
class Empleado:

    def __init__(self, salario):
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def set_salario(self, nuevo_salario):
        self.__salario = nuevo_salario

empleado = Empleado(1200)
print(empleado.get_salario())

empleado.set_salario(1500)
print(empleado.get_salario())

#Mini reto final
class Libro:

    def __init__(self, paginas):
        self.__paginas = paginas

    def get_paginas(self):
        return self.__paginas

libro = Libro(300)
print(libro.get_paginas())