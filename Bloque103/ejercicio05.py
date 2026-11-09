print("1. Sumar")
print("2. Restar")
print("3. Salir")

opcion = input("Elige una opción: ")

if opcion == "1":
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    print(f"Resultado: {a + b}")
elif opcion == "2":
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    print(f"Resultado: {a - b}")
elif opcion == "3":
    print("Saliendo del programa")
else:
    print("Opción no válida")
