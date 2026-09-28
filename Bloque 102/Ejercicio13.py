#Pedir datos
edad_str = "23"
altura_str = "1.75"
es_estudiante_str = "true"

# Convertir tipos:
edad = int(edad_str)
altura = float(altura_str)
es_estudiante = es_estudiante_str.lower() == "true"

# Cálcula peso e IMC
peso = 68.0
imc = peso / (altura ** 2)

#  Mostrar resultados
print("--- DATOS CONVERTIDOS ---")
print("Edad (int):", edad, type(edad))
print("Altura (float):", altura, type(altura))
print("¿Es estudiante? (bool):", es_estudiante, type(es_estudiante))

print("\n--- OPERACIÓN ARITMÉTICA ---")
print(f"IMC calculado con la altura de {altura} m: {imc:.2f}")