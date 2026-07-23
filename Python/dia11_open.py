#Escribir en un archivo de texto
archivo = open("notas.txt", "w")

archivo.write("Hola Pablo\n")
archivo.write("Bienvedido al dia 11")

archivo.close()

#Leer un archivo de texto
archivo = open("notas.txt", "r")

contenido = archivo.read()
print(contenido)

archivo.close()

#Mini Reto 1
archivo = open("mensaje.txt", "w")
archivo.write("Python")
archivo.close()

archivo = open("mensaje.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#With open
#with open(("notas.txt", "r")) as archivo:
#    print(archivo.read())

#Ejercicio 1
archivo = open("mi_presentacion.txt", "w")
archivo.write("Hola, Soy Pablo.\n")
archivo.write("Estoy aprendiendo Python.")
archivo.close()

archivo = open("mi_presentacion.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#Mini Reto 2
archivo = open("datos.txt", "w")

archivo. write("Uno\n")
archivo.write("Dos")

archivo.close()

archivo = open("datos.txt", "r")
print(archivo.read())
archivo.close()

#Agregar Informacion
archivo = open("datos.txt","a")

archivo.write("Tres\n")

archivo.close()

#Ejercicio 2
archivo = open("diario.txt","w")
archivo.write("Día 11\n")
archivo.close()

archivo = open("diario.txt","a")
archivo.write("Hoy aprendí a trabajar con archivos.")
archivo.close()

archivo = open("diario.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#Mini Reto 3
archivo = open("texto.txt", "w")
archivo.write("Hola")
archivo.close()

archivo = open("texto.txt", "a")
archivo.write("Mundo.")
archivo.close()

archivo = open("texto.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#Reto Final Día 11
archivo = open("prueba.txt", "w")
archivo.write("Python")
archivo.close()

archivo = open("prueba.txt", "w")
archivo.write("Curso")
archivo.close()

archivo = open("pruebas.txt","r")
print(archivo.read())
archivo.close