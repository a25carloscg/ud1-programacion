#Definición de la funciones
def saludar(nombre, formal=False):
    if formal:
        return f"Buenos días, {nombre}."
    else:
        return f"¡Hola, {nombre}!"
def demostracion_ambito(nombre):
    variable_ejemplo = "Estoy DENTRO de la función"
    print(f"Dentro de la función: variable_ejemplo = '{variable_ejemplo}'")
    return f"¡Hola, {nombre}!"

#Crear variable
variable_ejemplo = "Estoy FUERA de la función"

#LLamadas a la función
print("--- Prueba de la función saludar ---")
print(saludar("Carlos")) 
print(saludar("Carlos", formal=True))


print("\n--- Prueba de Ámbito (Scope) ---")
print(f"Antes de la función:  variable_ejemplo = '{variable_ejemplo}'")

demostracion_ambito("Ana")
print(f"Después de la función: variable_ejemplo = '{variable_ejemplo}'")
