def celsius_a_fahrenheit(grados: float) -> float:
    return grados * 9/5 + 32

# Pruebas de funcionamiento
print(f"23.5 float: {celsius_a_fahrenheit(23.5)}")
# Aunque pasemos un int, Python no lanza error en tiempo de ejecución
print(f"20 int: {celsius_a_fahrenheit(20)}") 
