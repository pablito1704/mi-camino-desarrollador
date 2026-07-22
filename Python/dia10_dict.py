#Ejemplo 1
persona = {
    "nombre": "Pablo",
    "edad": 21,
    "Ciudad" : "Guayaquil"
}
print(persona["nombre"])
print(persona["edad"])

#MODIFICAR VALORES
persona["edad"] = 22
print(persona["edad"])

#Mini reto 1
auto = {
    "marca": "Toyota",
    "modelo": "Corolla",
}
print(auto["marca"])

#Ejercicio 1
estudiante = {
    "nombre": "Pablo",
    "edad": 21,
    "carrera": "Desarrollo de Software"
    }
print(f"Nombre: {estudiante['nombre']}")
print(f"Edad: {estudiante['edad']}")
print(f"Carrera: {estudiante['carrera']}")

#Mini reto 2
persona = {
    "nombre": "Ana",
    "edad": 25
}

persona["edad"] = 26
print(persona["edad"])

#Agrega nueva clave
estudiante = {
    "nombre": "Pablo",
    "edad": 21
}

estudiante["ciudad"] = "Guayaquil"
print(estudiante)

#Ejercicio 2
producto = {
    "nombre": "Laptop",
    "precio": 850
}

producto["marca"] = "Lenovo"
print(producto)

#Mini reto 3 
animal = {
    "tipo": "Perro",
    "nombre": "Max"
}
print(animal["nombre"])

#Recorrer un Diccionairio - Recorre las claves
persona = {
    "nombre": "Pablo",
    "edad": 21,
    "ciuddad": "Guayaquil"
}
for clave in persona:
    print(clave)

#Recorrer un Diccionairio - Recorre los valores
persona = {
    "nombre": "Pablo",
    "edad": 21,
    "ciuddad": "Guayaquil"
}
for valor in persona.values():
    print(valor)

#Recorrer un Diccionairio - Recorre las claves y valores
persona = {
    "nombre": "Pablo",
    "edad": 21,
    "ciuddad": "Guayaquil"
}
for clave, valor in persona.items():
    print(clave, ":", valor)

#Ejercicio 3
persona = {
    "nombre": "Pablo",
    "edad": 21,
    "ciudad": "Guayaquil"
}
for clave, valor in persona.items():
    print(clave, ":", valor)

#Mini reto 4 
fruta = {
    "nombre": "Manzana",
    "color": "Rojo"
}
for clave in fruta:
    print(clave)

#Reto final
persona = {
    "nombre": "Pablo",
    "edad": 21
}
persona["edad"] = 22
persona["ciudad"] = "Guayaquil"

for clave, valor in persona.items():
    print(clave, ":", valor)