# Contador
intentos = 0

while True:
    intentos += 1
    entrada = input("Introduce un número entero positivo: ")
    
    try:
        #numero entero
        numero = int(entrada)
        
        #es positivo?
        if numero > 0:
            print(f"\n¡Correcto! El número es {numero}.")
            break  # Salimos del bucle si el valor es válido
        else:
            print("El número debe ser positivo. Inténtalo de nuevo.")
            
    except ValueError:
        print("El valor introducido no es un número entero. Inténtalo de nuevo.")

#Resultado
print(f"Has necesitado {intentos} intento(s).")
