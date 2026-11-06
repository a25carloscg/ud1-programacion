def calcular_edad(ano_nacimiento: int, ano_actual: int) -> int:
    try:
        if ano_actual < ano_nacimiento:
            raise ValueError
        return ano_actual - ano_nacimiento
    except ValueError:
        print("Error: El año de nacimiento no puede ser posterior al año actual.")
    except TypeError:
        print("Error: Los años deben ser números enteros.")

ano_nacimiento = int(input("Introducir año de nacimiento: "))
ano_actual = int(input("Introducir fecha actual: "))

calcular_edad(ano_nacimiento, ano_actual)
calcular_edad("1990", 2026)