def factorial(n):
    # Caso base: el factorial de 0 o 1 es siempre 1. Evita la recursión infinita.
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Comprobación de resultados
valores = [0, 1, 5, 7]
for v in valores:
    print(f"Número {v} -> Recursivo: {factorial(v)} | Iterativo: {factorial_iterativo(v)}")
