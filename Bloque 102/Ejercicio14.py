#  Pedir tiempo y definir constantes
tiempo = float(input("Introduce el tiempo transcurrido (en segundos): "))
GRAVEDAD = 9.8
ALTURA_INICIAL = 100.0 

# Cálculo de la altura
altura = ALTURA_INICIAL - 0.5 * GRAVEDAD * tiempo ** 2

# Mostrar el resultado
print(f"\nTras {tiempo} segundos, la altura del objeto es: {altura:.2f} metros")