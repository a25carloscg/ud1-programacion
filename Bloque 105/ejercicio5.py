def estadisticas(a, b, c):
    minimo = min(a, b, c)
    maximo = max(a, b, c)
    media = (a + b + c) / 3
    
    return minimo, maximo, media

# Solicitar os tres números ao usuario
try:
    num1 = float(input("Introduce o primeiro número: "))
    num2 = float(input("Introduce o segundo número: "))
    num3 = float(input("Introduce o terceiro número: "))
#devolver valores
    min_val, max_val, med_val = estadisticas(num1, num2, num3)
#Resultados
    print("\n--- Resultados ---")
    print(f"O valor mínimo é: {min_val}")
    print(f"O valor máximo é: {max_val}")
    print(f"A media é: {med_val}")
