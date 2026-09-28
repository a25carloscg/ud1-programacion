# Pedir edad, nota y usuario
edad = int(input("Introduce la edad: "))
nota = float(input("Introduce la nota: "))
usuario = input("Introduce el nombre de usuario: ")

print("\n--- RESULTADOS DE VALIDACIÓN ---")

# Mayoría de edad (>= 18)
print("Es mayor de edad:", edad >= 18)

# Nota aprobada (>= 5) y sobresaliente (>= 9)
if edad >= 9:
    print("sobresaliente")
elif edad >= 5:
    print("Aprobado")
else:
    print("No aprueba")

# Nombre de usuario con más de 3 caracteres y no vacío
print("El usuario tiene más de 3 caracteres y no está vacío:", len(usuario) > 3 and usuario != "")