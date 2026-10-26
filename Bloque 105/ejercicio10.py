def calcular_propina(cuenta, porcentaje=10, personas=1):
    total_con_propina = cuenta + (cuenta * porcentaje / 100)
    return total_con_propina / personas

# Pruebas con distintas combinaciones de argumentos con nombre
print(f"Solo cuenta (100€): {calcular_propina(100)}€ por persona.")
print(f"Cuenta (100€) y 4 personas: {calcular_propina(100, personas=4)}€ por persona.")
print(f"Cuenta (150€), 15% propina y 3 personas: {calcular_propina(150, porcentaje=15, personas=3)}€ por persona.")
