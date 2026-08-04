#Proyecto Integrador con Programación Orientada a Objetos
class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def mostrar(self):
        print(f"Producto: {self.__nombre}")
        print(f"Precio: ${self.__precio}")

producto = Producto("Laptop", 850)
producto.mostrar()

#Mini reto 1
class Producto:
    def __init__(self, nombre):
        self.__nombre = nombre

    def mostrar(self):
        print(self.__nombre)

producto = Producto("Mouse")
producto.mostrar()

#Ejercicio 1
class Libro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def mostrar(self):
        print(f"Titulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")

libro = Libro("Python desde Cero", "Juan Perez")
libro.mostrar()

#Mini reto 2
class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

pelicula = Pelicula("Spider-Man")
print(pelicula.get_nombre())

#Actualizar información con un setter
class Producto:

    def  __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

producto = Producto("Teclado")

print(producto.get_nombre())

producto.set_nombre("Teclado Mecánico")
print(producto.get_nombre())

#Ejercicio 2
class Celular:

    def __init__(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca

celular = Celular("Samsung")
print(celular.get_marca())

celular.set_marca("Apple")
print(celular.get_marca())

#Mini reto 3
class Ciudad:

    def __init__(self, nombre):
        self.__nombre = nombre

    def set_nombre(self, nuevo):
        self.__nombre = nuevo

    def get_nombre(self):
        return self.__nombre

ciudad = Ciudad("Quito")

ciudad.set_nombre("Guayaquil")

print(ciudad.get_nombre())

#Reto final del Día 17
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

cuenta = CuentaBancaria("Pablo", 500)

print(cuenta.get_titular())
print(cuenta.get_saldo())

cuenta.depositar(250)

print(cuenta.get_saldo())

#Mini reto final
class Curso:
    def __init__(self, nombre):
        self.__nombre  = nombre

    def get_nombre(self):
        return self.__nombre

curso = Curso("Python")

print(curso.get_nombre())