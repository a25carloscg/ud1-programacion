def raiz_cuadrada(numero: float | int) -> float:
    try:
        if numero < 0:
            raise ValueError 
        return numero ** (1/2)
    except TypeError:
        return "Error: Debes introducir un número"
    except ValueError:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"

n = float(input("Introducir número: "))
print(raiz_cuadrada(n))
print(raiz_cuadrada("16"))
