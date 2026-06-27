# OPERADORES MATEMATICOS
numero1 = 10
numero2 = 5

print("Suma: ", numero1 + numero2)
print("Resta: ", numero1 - numero2)
print("Multiplicación: ", numero1 * numero2)
print("División: ", numero1 / numero2)

# COMPARACIONES
edad = 21

print(edad > 18)
print(edad < 20)
print(edad == 21)
print(edad != 21)


# IF
edad = 21

if edad >= 18:
    print("Eres mayor de edad.")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print(f"Hola {nombre}, Eres mayor de edad.")
else:
    print(f"Hola {nombre}, Eres menor de edad.")