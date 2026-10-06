# Pedir datos
nota_tareas = float(input("Introduce la nota de las tareas: "))
nota_teoria = float(input("Introduce la nota del examen teórico: "))
nota_practica = float(input("Introduce la nota del examen práctico: "))

# Definir conversión
PESO_TAREAS = 0.15
PESO_TEORIA = 0.20
PESO_PRACTICA = 0.65

# Cálculo de la nota final y redondeo
nota_final_sin_redondear = (nota_tareas * PESO_TAREAS) + (nota_teoria * PESO_TEORIA) + (nota_practica * PESO_PRACTICA)
nota_final = round(nota_final_sin_redondear, 1)

#resultado
print(f"\nLa nota final ponderada es: {nota_final}")