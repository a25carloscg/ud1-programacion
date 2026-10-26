# Reinicio REPETIDOR
intentos = 0

while True:
    
    intentos += 1
    entrada = input("Introduce un número entero positivo: ")
    
    # VALIDACIÓN
    if not entrada.isdigit() or int(entrada) <= 0:
        print("Entrada no válida. Debe ser un entero mayor que cero.")
        continue
    break

# RESPUESTA
print(f"\n¡Perfecto! Has introducido el número {entrada}.")
print(f"Has necesitado {intentos} {'intento' if intentos == 1 else 'intentos'}.")