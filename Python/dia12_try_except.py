#Ejemplo de try y except

try:
    numero = int(input("Ingrese un número: "))
    print(numero)

except ValueError:
    print("Debe ingresar un número válido.")

#Mini Reto 1
try:
    numero = int(input("Ingrese un número: "))
    print(numero)

except ValueError:
    print("Número Inválido.")

#Ejercicio 1
try:
    numero = int(input("Ingrese un número: "))
    print(f"El número ingresado es: {numero}")

except ValueError:
    print("Error: Debe ingresar un número.")

#Mini reto 2
try: 
    edad = int(input("Ingrese su edad: "))
    print("Edad registrada:", edad)

except ValueError:
    print("Edad inválida.")

#Con else
try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("Número inválido.")
else:
    print("El número ingresado fue: ", numero)

#Ejercicio 2
try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("Error: Entrada inválida.")
else:
    print("Número guardado correctamente.")

#Mini Reto 3
try:
    numero = int(input("Número:"))
except ValueError:
    print("Error")
else:
    print("Correcto")

#finally
try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("Número inválido.")
else:
    print("Número Correcto.")
finally:
    print("Programa finalizado.")

#Reto final del Día 12
try:
    numero = int(input("Ingrese un número: "))
except ValueError:
    print("Número Incorrecto.")
else:
    print("Número Aceptado.")
finally:
    print("Fin del Programa. :D!")