def calcular_edad(ano_nacimiento: int, ano_actual: int) -> int:

    if not isinstance(ano_nacimiento, int) or not isinstance(ano_actual, int):
        raise TypeError("Los años deben ser números enteros.")

    if ano_nacimiento > ano_actual:
        raise ValueError("El año de nacimiento no puede ser posterior al año actual.")
    
    return ano_actual - ano_nacimiento



try:
    nacimiento_usuario = int(input("Introduce tu año de nacimiento: "))
    actual_usuario = int(input("Introduce el año actual: "))
    
    edad = calcular_edad(nacimiento_usuario, actual_usuario)
    print(f"Tienes o cumplirás {edad} años.")

except TypeError:
    print("Error: Los años deben ser números enteros.")
except ValueError:
    print("Error: El año de nacimiento no puede ser posterior al año actual.")


print("\nRealizando llamada de prueba: calcular_edad('1990', 2026)...")

try:
    Resultado = calcular_edad("1990", 2026)
    print(Resultado)
except:
    print('ERROR')

