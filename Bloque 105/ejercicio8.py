def pedir_entero_positivo(mensaje):
    while True:
        valor = int(input(mensaje))
        if valor >= 0:
            return valor
        print("El número debe ser positivo")

#Uso de la función para pedir dos datos diferentes
edad = pedir_entero_positivo("Introduce tu edad: ")
dinero = pedir_entero_positivo("Introduce la cantidad de dinero a ingresar: ")

print(f"Edad ingresada: {edad}. Dinero ingresado: {dinero}")
