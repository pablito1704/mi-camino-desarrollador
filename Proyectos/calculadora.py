continuar = "si"
while continuar == "si":

    print("==== CALCULADORA ====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")

    opcion = input("Seleccione una opción: ")

    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

        
    if opcion == "1":
        print(f"La Suma es: {numero1 + numero2}")

    elif opcion == "2":
        print(f"La Resta es: {numero1 - numero2}")

    elif opcion == "3":
        print(f"La Multiplicación es: {numero1 * numero2}")

    elif opcion == "4":
        if numero2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            print(f"La División es: {numero1 / numero2:.2f}")

    elif opcion == "5":
        print(f"La Potencia es: {numero1 ** numero2}")

    else:
            print("Opción Inválida.")

    continuar = input("¿Desea realizar otra operación? (Si/No): ").lower()

print("Gracias por usar la calculadora. ¡Hasta Luego!")