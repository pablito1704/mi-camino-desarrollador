nota = int(input("Ingrese la nota del estudiante: " ))

if nota >= 90:
    print("Excelente!")

elif nota >= 70:
    print("Aprobado!")
else:
    print("Reprobado!")

# Operador and

edad = 21
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede Conducir.")

#Operador or

es_admin = False
es_supervisor = True

if es_admin or es_supervisor:
    print("Acceso permitido.")

#Operador not

activo = True

print(not activo)

#Ejercicio con if, elif, else y and
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
tiene_licencia = input("¿Tiene licencia de conducir? (si/no): ").lower()

if edad >= 18 and tiene_licencia.lower() == "si":
    print(f"{nombre}, puede conducir.")
elif edad < 18:
    print(f"{nombre}, no puede conducir porque es menor de edad.")
else:
    print(f"{nombre}, no puede conducir porque no tiene licencia.")


#Clasificacion de edades

edad = int(input("Ingrese su edad: "))

if edad <13:
    print("Es un niño.")
elif edad < 20:
    print("Es un adolescente.")
elif edad < 65:
    print("Es un adulto.")
else:
    print("Es un adulto mayor.")