def resumen_numeros(a, b, c, d, e):
    """Devuelve una tupla con el valor máximo, el mínimo y la suma de los valores absolutos de cinco números."""
    maximo = max(a, b, c, d, e)
    minimo = min(a, b, c, d, e)
    suma_absolutos = abs(a) + abs(b) + abs(c) + abs(d) + abs(e)
    return maximo, minimo, suma_absolutos

# Prueba con números positivos y negativos
resultado = resumen_numeros(10, -5, 3, -1, 8)
print(f"Máximo, Mínimo, Suma Absolutos: {resultado}")
