class Libro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def mostrar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")

libro = Libro("Python", "Guido")

libro.mostrar()

#Mini Reto 1
class Libro:
    def __init__(self, titulo):
        self.__titulo = titulo

    def mostrar(self):
        print(f"Título: {self.__titulo}")

libro = Libro("El Principito")
libro.mostrar()

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
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")

libro = Libro("Hábitos Atómicos", "James Clear")
libro.mostrar()

#Mini reto 2
class Libro:
    def __init__(self, titulo):
        self.__titulo = titulo

    def  get_titulo(self):
        return self.__titulo

    def mostrar(self):
        print(f"Título: {self.__titulo}")

libro = Libro("Clean Code")
print(libro.get_titulo())

#Ejercicio 2
class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def mostrar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")

libro1 = Libro("Python", "Guido Van Rossum")
libro2 = Libro("Clean Code", "Robert Martin")

biblioteca = [libro1, libro2]

for libro in biblioteca:
    libro.mostrar()

#Minir Reto 3
class Libro:
    def __init__(self, titulo):
        self.__titulo = titulo

    def mostrar(self):
        print(self.__titulo)

libros = [
    Libro("A"),
    Libro("B")
]

for libro in libros:
    libro.mostrar()

#Reto final del Día 18
class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def mostrar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")

libro1 = Libro("Python", "Guido Van Rossum")
libro2 = Libro("Clean Code", "Robert Martin")
libro3 = Libro("Hábitos Atómicos", "James Clear")

biblioteca = [libro1, libro2, libro3]

for libro in biblioteca:
    libro.mostrar()

#Mini reto final
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def mostrar(self):
        print(self.__nombre)

personas = [
    Persona("Ana"),
    Persona("Luis")
]

for persona in personas:
    persona.mostrar()