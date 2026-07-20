compras = []

continuar = "si"

while continuar == "si":
    producto = input("Ingrese un producto: ")
    compras.append(producto)
    continuar = input("¿Desea agregar otro producto? (Si/No): ").lower()

print("\nLista de compras: ")

for producto in compras:
    print("-", producto)
