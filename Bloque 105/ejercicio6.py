def es_nombre_valido(texto):
    # True solo si no está vacío y no contiene dígitos
    return len(texto.strip()) > 0 and not any(char.isdigit() for char in texto)

# Bucle de registro de usuarios
while True:
    nombre = input("Introduce el nombre de usuario: ")
    if es_nombre_valido(nombre):
        break
    print("Nombre no válido. No puede estar vacío ni contener números.")

edad = int(input("Introduce la edad: "))
email = input("Introduce el email: ")

print(f"\nDatos registrados -> Nombre: {nombre}, Edad: {edad}, Email: {email}")
