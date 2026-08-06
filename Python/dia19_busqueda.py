#Biblioteca con búsqueda de libros

class Libro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def mostrar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")

libro1 = Libro("Python", "Guido Van Rossum")
libro2 = Libro("Clean Code", "Robert Martín")

biblioteca = [libro1, libro2]

buscar = "Python"

for libro in biblioteca:
    if libro.get_titulo() == buscar:
        libro.mostrar()

#Mini reto 1
class Libro:

    def __init__(self, titulo):
        self.__titulo = titulo

    def get_titulo(self):
        return self.__titulo

libro = Libro("Python")

print(libro.get_titulo())

#Ejercicio 1
class Libro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def mostrar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")


libro1 = Libro("Python","Guido Van Rossum")
libro2 = Libro("Clean Code", "Robert Martín")

biblioteca = [libro1, libro2]

buscar = input("Ingrese el título a buscar: ")

for libro in biblioteca:
    if libro.get_titulo() == buscar:
        print(f"Libro Encontrado:")
        libro.mostrar()

#Mini reto 2
numeros = [5, 10, 15]

buscar = 10

for numero in numeros:
    if numero == buscar:
        print("Encontrado")

#Saber si un libro no existe
class Libro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def mostrar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")


libro1 = Libro("Python","Guido Van Rossum")
libro2 = Libro("Clean Code", "Robert Martín")

biblioteca = [libro1, libro2]

buscar = input("Ingrese el título a buscar: ")

encontrado = False

for libro in biblioteca:
    if libro.get_titulo() == buscar:
        print("Libro Encontrado: ")
        libro.mostrar()
        encontrado = True

if not encontrado:
    print("Libro no encontrado.")

#Ejercicio 2
class Libro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def mostrar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")

libro1 = Libro("Python", "Guido Van Rossum")
libro2 = Libro("Clean Code", "Robert Martín")

biblioteca = [libro1, libro2]

buscar = input("Ingrese el título a buscar: ")

encontrado = False

for libro in biblioteca:
    if libro.get_titulo() == buscar:
        print("Libro Encontrado:")
        libro.mostrar()
        encontrado = True

if not encontrado:
    print("Libro no encontrado.")

#Reto final del Día 19
class Libro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def mostrar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")

libro1 = Libro("Python", "Guido Van Rossum")
libro2 = Libro("Clean Code", "Robert Martín")
libro3 = Libro("Hábitos Atómicos", "James Clear")

biblioteca = [libro1, libro2, libro3]

buscar = input("Ingrese el título a buscar: ")

encontrado = False

for libro in biblioteca:
    if libro.get_titulo() == buscar:
        print("Libro Encontrado:")
        libro.mostrar()
        encontrado = True

if not encontrado:
    print("Libro no encontrado.")

#Mini Reto Final
frutas = ["Manzana", "Pera", "Uva"]

buscar = "Pera"

encontrado = False

for fruta in frutas:
    if fruta == buscar:
        encontrado = True

print(encontrado)

