#Pedir número
entrada = input("Introduce un número: ")

try:
    #conversión a float
    numero = float(entrada)
except ValueError:
    
    print("Eso no es un número válido")
else:

    resultado = numero * 2
    #Resultado
    print(f"El doble es: {resultado}")