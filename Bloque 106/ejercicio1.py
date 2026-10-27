def realizar_division():

    try:
        #Pedir datos
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        #Operación
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
        #errores
    except ValueError:
        print("Error: Entrada no válida, por favor introduce números.")
        
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        #llamada a la función

realizar_division()