import random

def lanzar_dado(caras=6):
    return random.randint(1, caras)

# Simulación de tiradas
resultado_d6 = lanzar_dado()
resultado_d20 = lanzar_dado(20)

print(f"Resultado dado de 6 caras: {resultado_d6}")
print(f"Resultado dado de 20 caras: {resultado_d20}")
