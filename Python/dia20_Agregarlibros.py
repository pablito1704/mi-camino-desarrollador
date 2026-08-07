#Agregar libros a una biblioteca
class Libro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def mostrar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")

biblioteca = []

titulo = input("Ingrese el título: ")
autor = input("Ingrese el autor: ")

libro = Libro(titulo, autor)

biblioteca.append(libro)

for libro in biblioteca:
    libro.mostrar()

#Mini reto 1
numeros = []

numeros.append(10)

print(numeros)

#Ejercicio 1
class Libro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def mostrar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")

    def get_titulo(self):
        return self.__titulo

biblioteca = []

titulo = input("Ingrese el título: ")
autor = input("Ingrese el autor: ")

libro = Libro(titulo, autor)
biblioteca.append(libro)

for libro in biblioteca:
    libro.mostrar()

#Mini reto 2
frutas = []
frutas.append("Manzana")
frutas.append("Pera")

print(frutas)

#Agregar varios libros
biblioteca = []

continuar = "si"
while continuar == "si":

    titulo = input("Título: ")
    autor = input("Autor: ")

    libro = Libro(titulo, autor)

    biblioteca.append(libro)

    continuar = input("¿Agregar otro libro? (Si/No): ").lower()

for libro in biblioteca:
    libro.mostrar()

#Ejercicio 2
biblioteca = []

continuar = "si"
while continuar == "si":

    titulo = input("Título: ")
    autor = input("Autor: ")

    libro = Libro(titulo, autor)

    biblioteca.append(libro)

    continuar = input("¿Agregar otro libro? (Si/No): ").lower()

for libro in biblioteca:
    libro.mostrar()

#Mini Reto 3
numeros = []
continuar == "si"

while continuar == "si":
    numeros.append(1)
    continuar = "no"

print(numeros)

#Reto final del Día 20
class Libro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def mostrar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")

biblioteca = []

continuar = "si"

while continuar == "si":
    titulo = input("Ingrese el título: ")
    autor = input("Ingrese el autor: ")

    libro = Libro(titulo, autor)
    biblioteca.append(libro)

    continuar = input("¿Desea agregar otro libro? (Si/No): ").lower()

print("Biblioteca:")

for libro in biblioteca:
    libro.mostrar()


#Mini reto final
animales = []

animales.append("Perro")
animales.append("Gato")

for animal in animales:
    print(animal)