while True:
    # MOSTRAR OPCIONES
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    
    opcion = input("Elige una opción (1-3): ")
    #CALCULAR y MOSTRAR SOLUCIÓN
    if opcion == "1":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la suma es: {num1 + num2}")
    
    elif opcion == "2":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la resta es: {num1 - num2}")
    
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida")