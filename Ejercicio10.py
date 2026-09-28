#pedir datos (nombre, nivel, vida, esta vivo, vida máxima).

nombre = str(input("Ingrese su nombre: "))
nivel = int(input("Ingrese su nivel: "))
vida = float(input("Ingrese la cantidad de vida del personaje: "))
esta_vivo = bool(input("Ingrese si está vivo si está vivo (True) o (False): "))
#constante.

VIDA_MAXIMA = 100.0
#mostrar datos como script.

print("Nombre:", nombre)
print("Nivel:", nivel)
print("Vida:", vida)
print("¿Está vivo?:", esta_vivo)
print("Vida máxima:", VIDA_MAXIMA)