#EJEMPLO 1
def saludar():
    print("¡Hola, bienvenido al curso de Python.!")

saludar()

#EJEMPLO 2
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Pablo")
saludar("Ana")

#Mini Reto 1
def despedirse():
    print("Hasta luego.")

despedirse()

#Ejercicio 1
def presentarse(nombre):
    print(f"Hola, soy {nombre} y estoy aprendiendo Python.")

presentarse("Pablo")

#Mini Reto 2
def sumar():
    print(10 + 5)

sumar()
sumar()

#Ejemplo 1 return
def sumar(a ,b):
    return a + b

resultado = sumar(10, 5)
print(resultado)

#Ejercicio 2
def sumar(a, b):
    return a + b

resultado =  sumar(8, 12)
print(f"El resultado de la suma es: {resultado}")

#Mini Reto 3
def multiplicar(a ,b):
    return a * b

print(multiplicar(4, 5))

#Ejercicio 3
def es_mayor_de_edad(edad):
    if edad >=18:
        return True
    else:
        return False
    
print(es_mayor_de_edad(20))
print(es_mayor_de_edad(15))

#Mini Reto 4
def saludar(nombre):
    return f"Hola {nombre}"

mensaje = saludar("Pablo")
print(mensaje)

#RETO DEL DIA 9
def cuadrado(numero):
    return numero ** 2

resultado = cuadrado(6)
print(resultado)