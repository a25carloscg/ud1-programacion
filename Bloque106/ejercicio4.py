def procesar_edad(texto):
    try:
        edad = int(texto)
        return edad * 2
    except ValueError:
        print("Entrada no válida: ")
        return None
    finally:
        print("Intento de conversión finalizado")
#resultados LLamando a la función
resultado = procesar_edad(10)
print(resultado)
resultado = procesar_edad(k)
print(resultado)